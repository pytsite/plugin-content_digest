"""PytSite Content Digest Plugin Widgets
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang as _lang
from plugins import form as _form, widget as _widget


class Subscribe(_form.Form):
    """Subscribe Form
    """

    def _on_setup_form(self):
        if self.title is None:
            self.title = _lang.t('content_digest@subscribe_to_digest')

        self.prevent_submit = True
        self.css += ' widget-content-digest-subscribe'
        self.assets.extend([
            'content_digest@form.css',
            'content_digest@form.js',
        ])

    def _on_setup_widgets(self):
        self.add_widget(_widget.input.Email(
            uid='email',
            weight=10,
            label=_lang.t('content_digest@your_email'),
            label_hidden=True,
            placeholder=_lang.t('content_digest@your_email'),
            required=True,
        ))

        self.submit_button.form_area = 'body'
        self.submit_button.value = _lang.t('content_digest@ok')
        self.submit_button.icon = None
