"""PytSite Content Digest Plugin Events Handlers
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from datetime import datetime as _datetime, timedelta as _timedelta
from pytsite import reg as _reg, lang as _lang, logger as _logger, mail as _mail, tpl as _tpl
from plugins import odm as _odm, content as _content


def cron_weekly():
    """Send weekly mail digest.
    """
    model = _reg.get('content_digest.models')
    if not model:
        return

    app_name = _lang.t('app_name')
    entities_num = _reg.get('content_digest.entities_number', 10)
    pub_period = _datetime.now() - _timedelta(7)

    entities = []
    for model in _reg.get('content_digest.models', []):
        f = _content.find(model, language='*').gte('publish_time', pub_period).sort([('views_count', _odm.I_DESC)])
        entities += list(f.get(entities_num))

    for subscriber in _odm.find('content_subscriber').eq('enabled', True).get():
        _logger.info('Prepare content digest for {}'.format(subscriber.f_get('email')))

        lng = subscriber.f_get('language')
        m_subject = _lang.t('content_digest@weekly_digest_mail_subject', {'app_name': app_name}, lng)
        m_body = _tpl.render(_reg.get('content_digest.tpl', 'content_digest@digest'), {
            'entities': entities,
            'subscriber': subscriber,
            'language': lng,
        })
        _mail.Message(subscriber.f_get('email'), m_subject, m_body).send()
