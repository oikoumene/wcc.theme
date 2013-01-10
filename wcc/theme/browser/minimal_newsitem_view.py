from five import grok
from Products.ATContentTypes.interfaces.news import IATNewsItem
from dateutil.parser import parse
grok.templatedir('templates')

class MinimalNewsItemView(grok.View):
    grok.context(IATNewsItem)
    grok.name('minimal_newsitem_view')
    grok.template('minimal_newsitem_view')

    def date(self):
        return parse(self.context.Date()).strftime('%d %B %Y')
