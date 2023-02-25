from djangocms_site_importer.management.core.ElementParser import *

class ParagraphParser(ElementParser):
    ElementType = "p"
    def __init__(self, element, tag):
        super().__init__(element, tag)
    def print(self, pre=""):
        super(ParagraphParser, self).print(pre)

    def getPluginName(self):
        return "TextPlugin"
    
    def getPluginBody(self):
        return self.element.get_text()
    
    def createPlugin(self, parent, placeholder):
        from cms.api import add_plugin
        
        add_plugin(parent, self.getPluginName(), 'en', body=self.getPluginBody(), target=placeholder)
    
    def export(self):
        pass