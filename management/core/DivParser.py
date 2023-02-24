from djangocms_site_importer.management.core.ElementParser import *

class DivParser(ElementParser):
    ElementType = "div"
    def __init__(self, element, tag):
        super().__init__(element, tag)

    def print(self, pre=""):
        #print("This is " + __name__)
        super(DivParser, self).print(pre)


    def createPlugin(self, parent, placeholder):
        from cms.api import add_plugin

        print("CreatePlugin " + str(__class__))
        plugin = None

        if(self.getPluginName() == "GridRowPlugin"):
            plugin = add_plugin(parent, 'GridColumnPlugin', 'en', config={ "column_alignment" : "", "text_alignment" : "", "xs_col": None})
        elif(self.getPluginName() == "GridRowPlugin"):
            plugin = add_plugin(parent,'GridRowPlugin', 'en', config={ "vertical_alignment" : "", "horizontal_alignment" : ""})
        elif(self.getPluginName() == "GridContainer"):
            plugin = add_plugin(parent, 'GridContainerPlugin', 'en', config={"container_type": "section", "attributes": {"class" : self.getClass()}})
        
        return plugin
    
    def getPluginName(self):

        if(self.getClass().startswith("row")):
            return "GridRowPlugin"
        elif(self.getClass().startswith("col")):
            return "GridColumnPlugin"
        
        return "GridContainer"

    def export(self):
        pass