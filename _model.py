"""PytSite Content Digest Plugin Models
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from plugins import odm as _odm


class ContentDigestSubscriber(_odm.model.Entity):
    """content_digest_subscriber ODM Model
    """

    def _setup_fields(self):
        """Hook.
        """
        self.define_field(_odm.field.String('email', is_required=True))
        self.define_field(_odm.field.Bool('enabled', default=True))
        self.define_field(_odm.field.String('language', is_required=True))

    def _setup_indexes(self):
        """Hook.
        """
        self.define_index([('email', _odm.I_ASC), ('language', _odm.I_ASC)], unique=True)
