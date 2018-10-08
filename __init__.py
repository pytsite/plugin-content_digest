"""PytSite Content Digest Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from ._api import get_form


def plugin_load():
    from plugins import odm
    from . import _model

    # ODM models
    odm.register_model('content_digest_subscriber', _model.ContentDigestSubscriber)


def plugin_load_wsgi():
    from pytsite import router, cron
    from plugins import settings, http_api
    from . import _eh, _model, _settings_form, _controllers, _http_api_controllers

    # Event handlers
    cron.every_min(_eh.on_cron_every_min)

    # Routes
    router.handle(_controllers.Unsubscribe, '/content_digest/unsubscribe/<sid>', 'content_digest@unsubscribe')

    # HTTP API handlers
    http_api.handle('POST', 'content_digest/subscribe', _http_api_controllers.PostSubscribe,
                    'content_digest@post_subscribe')

    # Settings
    settings.define('content_digest', _settings_form.Form, 'content_digest@content_digest', 'fa fa-rocket')
