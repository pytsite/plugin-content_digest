"""PytSite Content Digest Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import plugman as _plugman

if _plugman.is_installed(__name__):
    # Public API
    from . import _widget as widget


def plugin_load():
    from pytsite import lang, tpl
    from plugins import assetman

    # Resources
    lang.register_package(__name__)
    tpl.register_package(__name__)

    assetman.register_package(__name__)
    assetman.js_module('content-digest-widget-subscribe', __name__ + '@js/content-digest-widget-subscribe')
    assetman.t_less(__name__)
    assetman.t_js(__name__)


def plugin_load_uwsgi():
    from pytsite import router, cron
    from plugins import permissions, odm, settings, http_api
    from . import _eh, _model, _settings_form, _controllers, _http_api_controllers

    # ODM models
    odm.register_model('content_subscriber', _model.ContentSubscriber)

    # Event handlers
    cron.weekly(_eh.cron_weekly)

    # Routes
    router.handle(_controllers.Unsubscribe, '/content_digest/unsubscribe/<sid>', 'content_digest@unsubscribe')

    # HTTP API handlers
    http_api.handle('POST', 'content_digest/subscribe', _http_api_controllers.PostSubscribe,
                    'content_digest@post_subscribe')

    # Permissions
    permissions.define_permission('content_digest@manage_settings', 'content_digest@manage_content_digest_settings',
                                  'app')

    # Settings
    settings.define('content_digest', _settings_form.Form, 'content_digest@content_digest', 'fa fa-rocket',
                    'content_digest@manage_settings')


def plugin_install():
    from plugins import assetman

    plugin_load()
    assetman.build(__name__)
    assetman.build_translations()
