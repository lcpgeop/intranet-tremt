from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel import model
from tremt.intranet import _
from zope import schema
from zope.interface import implementer


class IArea(model.Schema):
    """Definicao de uma Area."""

    model.fieldset(
        "contato",
        _("Contato"),
        fields=[
            "email",
            "telefone",
        ],
    )
    email = Email(
        title=_("Email"),
        required=True,
    )

    telefone = schema.TextLine(
        title=_("Telefone"),
        description=_("Informe o telefone de contato"),
        required=False,
    )


@implementer(IArea)
class Area(Container):
    """Uma Area no TRE-MT."""
