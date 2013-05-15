# This package may contain traces of nuts

from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from wcc.theme.interfaces import IThemeSettings

def getSettings():
    registry = getUtility(IRegistry)
    try:
        return registry.forInterface(IThemeSettings)
    except:
        registry.registerInterface(IThemeSettings)
    return registry.forInterface(IThemeSettings)

