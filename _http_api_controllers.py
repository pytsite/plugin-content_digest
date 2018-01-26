"""PytSite Content Digest HTTP API Controllers
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import validation as _validation, lang as _lang, routing as _routing
from plugins import odm as _odm


class PostSubscribe(_routing.Controller):
    """Subscribe to digest
    """

    def exec(self) -> dict:
        lng = _lang.get_current()
        email = _validation.rule.Email(value=self.arg('email')).validate()

        # Search for subscriber
        s = _odm.find('content_subscriber').eq('email', email).eq('language', lng).first()

        # Create new subscriber
        if not s:
            s = _odm.dispense('content_subscriber').f_set('email', email).f_set('language', lng).save()

        # Enable subscriber
        s.f_set('enabled', True).save()

        return {'message': _lang.t('content_digest@digest_subscription_success')}
