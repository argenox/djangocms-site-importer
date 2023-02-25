from djangocms_site_importer.management.core.TextParser import *

class olParser(TextParser):
    ElementType = "ol"
    def __init__(self, element, tag):
        super().__init__(element, tag)
        self.ElementType = "ol"

    
   