from djangocms_site_importer.management.core.TextParser import *

class linkParser(TextParser):
    ElementType = "a"
    def __init__(self, element, tag):
        super().__init__(element, tag)
        self.ElementType = "a"

    
   