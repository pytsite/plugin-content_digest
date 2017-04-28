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

        self._css += ' widget-content-digest-subscribe'
        self._js_module = 'content-digest-widget-subscribe'

    def _get_element(self, **kwargs):
        root = _html.TagLessElement()

        root.append(_html.H3(self.title, css='widget-title'))

        form = _html.Form()
        form.append(_html.Label(_lang.t('content_digest@your_email'), css='sr-only'))
        form.append(_html.Input(
            type='text',
            name='email',
            css='form-control',
            placeholder=_lang.t('content_digest@your_email'),
            required=True,
        ))
        form.append(_html.Button(
            content=_lang.t('content_digest@ok'),
            css='btn btn-primary',
            type='submit',
        ))

        root.append(form)

        return root
