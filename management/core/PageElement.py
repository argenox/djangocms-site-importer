class PageElement:
    
    def __init__(self):
        self.parse_tree = []
        self.title = ""

    def addTreeItem(self, item):
        self.parse_tree.append(item)
    
    def setTitle(self, title):
        self.title = title