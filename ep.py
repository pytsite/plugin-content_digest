"""
"""
from pytsite import http as _http, odm as _odm, router as _router, lang as _lang

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def unsubscribe(args: dict, inp: dict) -> _http.response.Redirect:
    """Unsubscribe from content digest.
    """
    s = _odm.dispense('content_subscriber', args.get('id'))
    if s:
        with s:
            s.f_set('enabled', False).save()
        _router.session().add_success_message(_lang.t('content_digest@unsubscription_successful'))

    return _http.response.Redirect(_router.base_url())
