from djangocms_site_importer.management.core.TextParser import *

class liParser(TextParser):
    ElementType = "li"
    def __init__(self, element, tag):
        super().__init__(element, tag)
        self.ElementType = "li"

    
   