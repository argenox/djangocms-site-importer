from djangocms_site_importer.management.core.TextParser import *

class liParser(TextParser):
    ElementType = "li"
    def __init__(self, element, tag, filepath):
        super().__init__(element, tag, filepath)
        self.ElementType = "li"

    def allowChildren(self):
            return False

    
   