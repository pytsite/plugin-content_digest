"""PytSite Content Digest Plugin.
"""
# Public API
from . import _widget as widget

from pytsite import events as _events, odm as _odm, http_api as _http_api, router as _router, lang as _lang, \
    tpl as _tpl, assetman as _assetman, permissions as _permissions, settings as _settings
from . import _eh, _model, _settings_form

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Resources
_lang.register_package(__name__, alias='content_digest')
_tpl.register_package(__name__, alias='content_digest')
_assetman.register_package(__name__, alias='content_digest')

# ODM models
_odm.register_model('content_subscriber', _model.ContentSubscriber)

# Event handlers
_events.listen('pytsite.cron.weekly', _eh.cron_weekly)

# Routes
_router.add_rule('/content_digest/unsubscribe/<id>', 'content_digest@unsubscribe', __name__ + '@unsubscribe')

# HTTP API handlers
_http_api.register_handler('content_digest', __name__ + '.http_api')

# Permissions
_permissions.define_permission('content_digest.settings.manage', 'content_digest@manage_content_digest_settings', 'app')

# Settings
_settings.define('content_digest', _settings_form.Form, 'content_digest@content_digest', 'fa fa-rocket',
                'content_digest.settings.manage')
