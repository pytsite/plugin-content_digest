"""PytSite Content Digest Plugin Settings Form
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang as _lang
from plugins import content as _content, settings as _settings, widget as _widget


class Form(_settings.Form):
    def _on_setup_widgets(self):
        """Hook
        """
        self.add_widget(_widget.select.Checkboxes(
            uid='setting_days_of_week',
            weight=10,
            label=_lang.t('content_digest@days_of_week'),
            int_keys=True,
            items=[
                (0, _lang.t('pytsite.lang@weekday_monday')),
                (1, _lang.t('pytsite.lang@weekday_tuesday')),
                (2, _lang.t('pytsite.lang@weekday_wednesday')),
                (3, _lang.t('pytsite.lang@weekday_thursday')),
                (4, _lang.t('pytsite.lang@weekday_friday')),
                (5, _lang.t('pytsite.lang@weekday_saturday')),
                (6, _lang.t('pytsite.lang@weekday_sunday')),
            ],
            default='0',
        ))

        self.add_widget(_widget.select.DateTime(
            uid='setting_day_time',
            weight=20,
            label=_lang.t('content_digest@time'),
            default='08:00',
            datepicker=False,
            h_size='col-sm-2 col-lg-1'
        ))

        self.add_widget(_widget.input.Integer(
            uid='setting_entities_number',
            weight=30,
            label=_lang.t('content_digest@entities_number'),
            min=1,
            default=10,
            h_size='col-sm-2 col-lg-1'
        ))

        self.add_widget(_content.widget.ModelCheckboxes(
            uid='setting_models',
            weight=40,
            label=_lang.t('content_digest@content_models'),
            filter=lambda entity: entity.has_field('views_count'),
        ))

        w = 50
        for lang_code in _lang.langs():
            self.add_widget(_widget.input.Text(
                uid='setting_mail_subject_{}'.format(lang_code),
                weight=w,
                label=_lang.t('content_digest@mail_subject', {'lang': _lang.lang_title(lang_code)}),
                default=_lang.t('content_digest@default_mail_subject', language=lang_code)
            ))
            w += 1

        super()._on_setup_widgets()
