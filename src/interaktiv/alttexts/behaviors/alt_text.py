from interaktiv.alttexts import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.interface import Interface
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider


@provider(IFormFieldProvider)
class IAltTextBehavior(model.Schema):
    alt_text = schema.TextLine(
        title=_("alt_text_label", default="Alt text"),
        description="",
        required=False,
        default="",
    )


class IAltTextMarker(Interface):
    """Marker interface for content that supports alt text."""


@implementer(IAltTextBehavior)
class AltTextAdapter:
    def __init__(self, context):
        self.context = context

    @property
    def alt_text(self):
        return self.context.alt_text

    @alt_text.setter
    def alt_text(self, value):
        self.context.alt_text = value
