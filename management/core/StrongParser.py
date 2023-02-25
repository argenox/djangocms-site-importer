from djangocms_site_importer.management.core.TextParser import *

class StrongParser(TextParser):
    ElementType = "strong"
    def __init__(self, element, tag):
        super().__init__(element, tag)
        self.ElementType = "strong"

    
   