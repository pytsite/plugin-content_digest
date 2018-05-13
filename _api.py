"""PytSite Content Digest Plugin API Functions
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import router as _router
from . import _frm


def get_form(**kwargs):
    """Get subscribe form
    """
    return _frm.Subscribe(_router.request(), **kwargs)
