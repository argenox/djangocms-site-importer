from djangocms_site_importer.management.core.ElementParser import *

class TextParser(ElementParser):
    ElementType = "p"
    def __init__(self, element, tag):
        super().__init__(element, tag)
    
    def print(self, pre=""):        
        super(TextParser, self).print(pre)

    def export(self):
        pass