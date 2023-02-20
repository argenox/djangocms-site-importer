from djangocms_site_importer.management.core.ElementParser import *

class SectionParser(ElementParser):
    ElementType = "section"
    def __init__(self, element, tag):
        super().__init__(element, tag)

    def print(self, pre=""):
        #print("This is " + __name__)
        super(SectionParser, self).print(pre)

    def export(self):
        pass