from djangocms_site_importer.management.core.ElementParser import *

class ParagraphParser(ElementParser):
    ElementType = "p"
    def __init__(self, element, tag):
        super().__init__(element, tag)
    def print(self, pre=""):        
        super(ParagraphParser, self).print(pre)

    def export(self):
        pass