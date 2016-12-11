"""PytSite Content Digest HTTP API Endpoints.
"""
from pytsite import validation as _validation, lang as _lang, odm as _odm

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def post_subscribe(**kwargs) -> dict:
    """Subscribe to digest endpoint.
    """
    lng = _lang.get_current()
    email = _validation.rule.Email(value=kwargs.get('email')).validate()

    # Search for subscriber
    s = _odm.find('content_subscriber').eq('email', email).eq('language', lng).first()

    # Create new subscriber
    if not s:
        s = _odm.dispense('content_subscriber').f_set('email', email).f_set('language', lng).save()

    # Enable subscriber
    with s:
        s.f_set('enabled', True).save()

    return {'message': _lang.t('content_digest@digest_subscription_success')}
