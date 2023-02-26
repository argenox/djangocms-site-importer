from djangocms_site_importer.management.core.ElementParser import *

class TextParser(ElementParser):
    ElementType = "p"
    def __init__(self, element, tag, filepath):
        super().__init__(element, tag, filepath)
    
    def print(self, pre=""):        
        super(TextParser, self).print(pre)

    def getPluginName(self):
        return "TextPlugin"
    
    def allowChildren(self):
            return False
    
    def getPluginBody(self):
        return self.element
        #return self.element.get_text()
    
    def createPlugin(self, parent, placeholder):
        from cms.api import add_plugin
        
        pbody = self.getPluginBody() #"<" + self.tag + " " + self.getAttributesStr() + "> " + self.getPluginBody() + "</" + self.tag + ">"
        #print("heADING BODY: " + body)

        add_plugin(parent, 
                   self.getPluginName(), 
                   'en', 
                   body=pbody, 
                   target=placeholder)
    
    def export(self):
        pass