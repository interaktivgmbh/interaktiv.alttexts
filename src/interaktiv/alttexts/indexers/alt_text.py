from plone.app.contenttypes.interfaces import IImage
from plone.indexer import indexer


@indexer(IImage)
def alt_text_indexer(obj):
    return getattr(obj, 'alt_text', '')
