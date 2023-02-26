from djangocms_site_importer.management.core.TextParser import *

class linkParser(TextParser):
    ElementType = "a"
    def __init__(self, element, tag, filepath):
        super().__init__(element, tag, filepath)
        self.ElementType = "a"

    def allowChildren(self):
            return True

    
   