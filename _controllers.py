"""
"""
from pytsite import routing as _routing, odm as _odm, router as _router, lang as _lang

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Unsubscribe(_routing.Controller):
    def exec(self):
        """Unsubscribe from content digest
        """
        s = _odm.dispense('content_subscriber', self.arg('uid'))
        if s:
            with s:
                s.f_set('enabled', False).save()
            _router.session().add_success_message(_lang.t('content_digest@unsubscription_successful'))

        return self.redirect(_router.base_url())
