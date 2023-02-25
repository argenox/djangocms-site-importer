from djangocms_site_importer.management.core.TextParser import *

class iParser(TextParser):
    ElementType = "i"
    def __init__(self, element, tag):
        super().__init__(element, tag)
        self.ElementType = "i"

    
   