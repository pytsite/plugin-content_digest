"""PytSite Content Digest Plugin Events Handlers
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from datetime import datetime as _datetime, timedelta as _timedelta
from pytsite import reg as _reg, lang as _lang, logger as _logger, mail as _mail, tpl as _tpl, util as _util
from plugins import odm as _odm, content as _content


def on_cron_every_min():
    """Send weekly mail digest
    """
    # Check if the models is specified
    models = _reg.get('content_digest.models')
    if not models:
        return

    # Check for the current day and time
    weekdays = _reg.get('content_digest.days_of_week', [])  # type: list
    time_of_day = _reg.get('content_digest.day_time', '00:00')
    if isinstance(time_of_day, _datetime):
        time_of_day = time_of_day.time()
    else:
        time_of_day = _util.parse_date_time(time_of_day).time()
    now = _datetime.now()
    now_weekday = now.weekday()

    # if now.weekday() not in weekdays or not (time_of_day.hour == now.hour and time_of_day.minute == now.minute):
    #     return

    # Calculate days number to query collections
    prev_weekday = weekdays[weekdays.index(now_weekday) - 1]
    if prev_weekday < now_weekday:
        days_diff = (now_weekday + 1) - (prev_weekday + 1)
    else:
        days_diff = 8 - (prev_weekday + 1) + now_weekday

    # Get entities of each model
    entities = []
    entities_num = _reg.get('content_digest.entities_number', 10)
    pub_period = _datetime.now() - _timedelta(days_diff)
    for model in models:
        f = _content.find(model, language='*').gte('publish_time', pub_period).sort([('views_count', _odm.I_DESC)])
        entities += list(f.get(entities_num))

    # Sort all entities and cut top
    entities = sorted(entities, key=lambda e: e.views_count)[:entities_num]

    for subscriber in _odm.find('content_digest_subscriber').eq('enabled', True).get():
        _logger.info('Preparing content digest for {}'.format(subscriber.f_get('email')))

        lng = subscriber.f_get('language')
        default_m_subject = _lang.t('content_digest@default_mail_subject', lng)
        m_subject = _reg.get('content_digest.mail_subject_{}'.format(lng), default_m_subject)
        m_body = _tpl.render(_reg.get('content_digest.tpl', 'content_digest@digest'), {
            'entities': entities,
            'subscriber': subscriber,
            'language': lng,
        })
        _mail.Message(subscriber.f_get('email'), m_subject, m_body).send()
