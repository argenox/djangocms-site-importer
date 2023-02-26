from djangocms_site_importer.management.core.TextParser import *

class tableParser(TextParser):
    ElementType = "table"
    def __init__(self, element, tag, filepath):
        super().__init__(element, tag, filepath)
        self.ElementType = "table"

    def allowChildren(self):
            return False

    
   