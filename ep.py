"""
"""
from pytsite import http as _http, odm as _odm, router as _router, lang as _lang

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def unsubscribe(sid: str) -> _http.response.Redirect:
    """Unsubscribe from content digest.
    """
    s = _odm.dispense('content_subscriber', sid)
    if s:
        with s:
            s.f_set('enabled', False).save()
        _router.session().add_success_message(_lang.t('content_digest@unsubscription_successful'))

    return _http.response.Redirect(_router.base_url())
