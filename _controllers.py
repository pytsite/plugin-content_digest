"""PytSite Content Digest Plugin Controllers
"""
from pytsite import routing as _routing, router as _router, lang as _lang
from plugins import odm as _odm

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Unsubscribe(_routing.Controller):
    def exec(self):
        """Unsubscribe from content digest
        """
        s = _odm.dispense('content_subscriber', self.arg('uid'))
        if s:
            s.f_set('enabled', False).save()
            _router.session().add_success_message(_lang.t('content_digest@unsubscription_successful'))

        return self.redirect(_router.base_url())
