"""PytSite Content Digest Plugin Widgets.
"""
from pytsite import widget as _pytsite_widget, html as _html, lang as _lang

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Subscribe(_pytsite_widget.Abstract):
    """Subscribe Form.
    """

    def __init__(self, uid: str = 'content-digest-subscribe', **kwargs):
        """Init.
        """
        kwargs['title'] = kwargs.get('title', _lang.t('content_digest@subscribe_to_digest'))

        super().__init__(uid, **kwargs)

        self.css += ' widget-content-digest-subscribe'
        self.assets.append('content_digest@css/widget.css')
        self.assets.append('content_digest@js/widget.js')

    def get_html_em(self, **kwargs):
        root = _html.TagLessElement()

        root.append(_html.H3(self.title, cls='widget-title'))

        form = _html.Form()
        form.append(_html.Label(_lang.t('content_digest@your_email'), cls='sr-only'))
        form.append(_html.Input(
            type='text',
            name='email',
            cls='form-control',
            placeholder=_lang.t('content_digest@your_email'),
            required=True,
        ))
        form.append(_html.Button(
            content=_lang.t('content_digest@ok'),
            cls='btn btn-primary',
            type='submit',
        ))

        root.append(form)

        return root
