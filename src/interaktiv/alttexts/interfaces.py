"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.app.contenttypes.interfaces import IPloneAppContenttypesLayer


class IInteraktivAltTextBrowserLayer(IPloneAppContenttypesLayer, IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
