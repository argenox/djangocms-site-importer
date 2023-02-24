class ElementParser:
    ElementType = "h"
    def __init__(self, element, tag):
        self.element = element
        self.tag = tag
        self.children = []
        self.class_info = self.joinClass(self.element.get("class"))

    def getClass(self):
        return self.element.attrs.get("class")[0]
    
    def getPluginName(self):
        return ""
    
    def getPluginBody(self):
        return ""
    
    def getChildren(self):
        return self.children
    
    def joinClass(self, list):
        str = ""

        if(list != None and len(list) > 0):
            for i in list:
                str += " " + i

        return str
        
    @classmethod
    def getElementType(cls):        
        return cls.ElementType
    
    def hasChildren(self):
        if(self.children != None and len(self.children) > 0):
            return True
        else:
            return False
        
    def print(self, pre=""):    
        if(self.element.has_attr('class')):
            print(pre + self.tag + self.class_info)  
        else:
            print(pre + self.tag)
        for c in self.children:
            c.print(pre + "\t")

    def createPlugin(self, parent, placeholder):
        pass

    def export(self):
        pass

        