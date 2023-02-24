from djangocms_site_importer.management.core.ElementParser import *

class SectionParser(ElementParser):
    ElementType = "section"
    def __init__(self, element, tag):
        super().__init__(element, tag)

    def print(self, pre=""):
        #print("This is " + __name__)
        super(SectionParser, self).print(pre)
    
    def getPluginName(self):
        return "GridContainerPlugin"
    
    def getPluginBody(self):
        return ""
    
    def createPlugin(self, parent, placeholder):
        from cms.api import add_plugin
        
        add_plugin(parent, self.getPluginName(), 'en', body=self.element, target=placeholder)


    def export(self):
        pass