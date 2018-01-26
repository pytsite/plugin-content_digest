"""PytSite Content Digest Plugin Settings Form
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang as _lang
from plugins import content as _content, settings as _settings, widget as _widget


class Form(_settings.Form):
    def _on_setup_widgets(self):
        """Hook.
        """
        self.add_widget(_widget.input.Integer(
            uid='setting_entities_number',
            weight=10,
            label=_lang.t('content_digest@entities_number'),
            min=1,
            default=10,
            h_size='col-sm-2 col-lg-1'
        ))

        self.add_widget(_content.widget.ModelCheckboxes(
            uid='setting_models',
            weight=20,
            label=_lang.t('content_digest@content_models'),
        ))

        super()._on_setup_widgets()
