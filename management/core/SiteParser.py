import os
from bs4 import BeautifulSoup
import bs4

import djangocms_site_importer.management.core.PageParser

from djangocms_site_importer.management.core.SiteParser import *
from djangocms_site_importer.management.core.PageParser import *
from djangocms_site_importer.management.core.ElementParser import *
from djangocms_site_importer.management.core.HeadingParser  import *
from djangocms_site_importer.management.core.ParagraphParser import *
from djangocms_site_importer.management.core.SectionParser import *
from djangocms_site_importer.management.core.TextParser import *
from djangocms_site_importer.management.core.DivParser import *
from djangocms_site_importer.management.core.PageElement import *

class SiteParser:

    parse_tree = []

    file_list = []

    page_list = []

    def __init__(self, dir):
        self.html_dir = dir
        self.page_list = []

    def parseDir(self):
        for subdir, dirs, files in os.walk(self.html_dir):
            for file in files:
                print(os.path.join(subdir, file))
                self.parseFile(subdir, file)
                self.printTree()
                break
            break

    def parseSection(self, section, tag, parent=None):

        if(tag != None and tag != "None"):
            print("Parsing Tag")
            for p in self.parser_list:
                
                #print("THis: " + HeadingParser.getElementType())
                #print("tag: " + tag)

                #print("Does it start? " + str(tag.startswith(p.getElementType())))
                if(tag.startswith(p.getElementType())):
                    
                    print("Tag Starts with it " + p.getElementType())
                    # instantiate it
                    #print(p.getElementType())
                    parser_object = type(p)

                    klass = globals()[p.__name__]
                    instance = klass(section, tag)
                    #instance.print()

                    if(parent is None):
                        #print("Top")
                        self.parse_tree.append(instance)
                    else:
                        #print("Child of ")
                        #parent.print()
                        parent.children.append(instance)

                    for child in section:
                        #print("CHild Type:" + str(type(child)))
                        #print("=================================================")
                        #print(child)
                        #print("=================================================")
                        #if child != None and child.name != None:
                        if type(child) is not bs4.element.NavigableString:
                            print("Parsing  child  " + child.name)
                            #print("parsing child in section" + str(child))
                            #if(child.tag != "None"):
                            #print("Child Name: " + child.name)
                            #print("Child Tag: " + child.tag )
                            self.parseSection(child, child.name, parent=instance)

    def printTree(self):
        print("Tree")
        for t in self.parse_tree:
            t.print()

    def parseFile(self, dir, filename):
        print("Parse File")
        parse_tree = []
        filepath = os.path.join(dir, filename)
        if(filename.endswith('.html')):
            file_list = []

            pe = PageElement()

            pparser = PageParser(filepath)
            pparser.parseFile()

            pe.setTitle(pparser.page_name)
            pe.addTreeItem(pparser.parse_tree)
            #parse_tree.append(pparser.parse_tree)
            #file_list.append(pparser)

            self.page_list.append(pe)
