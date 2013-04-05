from zope import schema
from zope.interface import Interface

class IThemeSettings(Interface):
    scheme = schema.Choice(title=u"Color scheme",
            vocabulary="wcc.theme.colorscheme",
            default='red')

    is_subsite = schema.Bool(
            title=u'Is Subsite',
            default=True
    )

class IThemeSpecific(Interface):
    pass
