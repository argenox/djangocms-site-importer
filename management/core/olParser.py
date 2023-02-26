from djangocms_site_importer.management.core.TextParser import *

class olParser(TextParser):
    ElementType = "ol"
    def __init__(self, element, tag, filepath):
        super().__init__(element, tag, filepath)
        self.ElementType = "ol"

    def allowChildren(self):
            return False

    
   