from djangocms_site_importer.management.core.TextParser import *

class StrongParser(TextParser):
    ElementType = "strong"
    def __init__(self, element, tag, filepath):
        super().__init__(element, tag, filepath)
        self.ElementType = "strong"

    
   