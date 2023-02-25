class ElementParser:
    ElementType = "h"
    def __init__(self, element, tag):
        self.element = element
        self.tag = tag
        self.children = []
        
    def getClass(self):
        return ' '.join(self.element.attrs.get("class"))
    
    def getStyle(self):
        style = self.element.attrs.get("style")
        if(style != None and len(style) > 0):
            return ' '.join(self.element.attrs.get("style"))
        return ""
    
    def getAttributes(self):

        at = self.element.attrs
        new_dict = {}
        if(at != None and len(at) > 0):

            for k, vals in at.items():
                new_dict[k] = " ".join(vals)
        return new_dict
    
    def getAttributesStr(self):
        at = self.element.attrs
        at_str = ""
        if(at != None and len(at) > 0):

            for k, vals in at.items():
                #print(k, vals)
                at_str += k.lower() + "=\"" + " ".join(vals) + "\" "

            # keys = at.keys()
            # vals = at.values()
            # for x in range (0, len(keys)):            
            #     print("key: " + keys[x] + "value: " + vals[x])
            #     at_str += keys[x] + "=\"" + vals[x] + "\" "
        #print("Attrib: " + at_str)
        return at_str

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
    
    def allowChildren(self):
            return True
        
    def print(self, pre=""):    
        if(self.element.has_attr('class')):
            print(pre + self.tag + self.getClass())  
        else:
            print(pre + self.tag)
        for c in self.children:
            c.print(pre + "\t")

    def createPlugin(self, parent, placeholder):
        pass

    def export(self):
        pass

        