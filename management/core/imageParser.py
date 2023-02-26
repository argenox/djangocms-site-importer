import os
from djangocms_site_importer.management.core.ElementParser import *
from django.contrib.auth.models import User
from django.core.files import File
from filer.fields.image import FilerImageField
from filer.models import Image
from django.db import models

class imageParser(ElementParser):
    ElementType = "img"
    def __init__(self, element, tag, filepath):
        super().__init__(element, tag, filepath)
        self.ElementType = "img"

    def allowChildren(self):
            return False
    
    def getPluginName(self):
        return "ImagePlugin"

    def createPlugin(self, parent, placeholder):
        from cms.api import add_plugin

        print("Adding Image Plugin")
        print("Body: " + self.getPluginBody()) 

        images = self.element.findAll('img')

        print("Src: " + self.element['src'])
        # Print alternate text
        print("Alt: " + self.element['alt'])

        image_path = self.element['src'].replace('\\','/') #os.path.basename(self.element['src'])
        image_alt = self.element['alt']

        head, tail = os.path.split(self.filepath)

        image_file_path = head + "\\.." + image_path     
        image_file_path = image_file_path.replace('/','\\')
        print("image Folder: " + image_file_path)

        if(os.path.isfile(image_file_path)):
             print("Adding Image")
             user = User.objects.get(username='developer')
             filepath, filename = os.path.split(image_file_path)
             with open(image_file_path, "rb") as f:
                 file_obj = File(f, name=filename)
                 image = Image.objects.create(owner=user,
                                            original_filename=filename,
                                            file=file_obj)
                 #instance = FilerImageField(null=True, blank=True, on_delete=models.DO_NOTHING)
                 image.save()

                 image_url = image.url
                 print("URL: " + image_url)
                 
        else:
             print("Not Adding Image")

        
        # pbody = self.getPluginBody() #"<" + self.tag + " " + self.getAttributesStr() + "> " + self.getPluginBody() + "</" + self.tag + ">"
        # #print("heADING BODY: " + body)

        # add_plugin(parent, 
        #            self.getPluginName(), 
        #            'en', 
        #            body=pbody, 
        #            target=placeholder)
        
        # plugin = add_plugin(parent, 
        #                     self.getPluginName(), 
        #                     'en', 
        #                     target=placeholder, 
        #                     config={"container_type": self.getSectionName(), "attributes": self.getAttributes()})
        
        # {"template": "default", "picture": {"model": "filer.image", "pk": 1}, "external_picture": "", "lazy_loading": false, "width": null, "height": null, "alignment": "start", "caption_text": "", "link_attributes": {}, "use_automatic_scaling": false, "use_crop": false, "use_no_cropping": false, "use_upscale": false, "use_responsive_image": "inherit", "thumbnail_options": null, "picture_fluid": true, "picture_rounded": false, "picture_thumbnail": false, "attributes": {}, "external_link": "", "internal_link": "", "file_link": null, "anchor": "", "mailto": "", "phone": "", "target": "", "responsive_visibility": null, "margin_x": "", "margin_y": "", "margin_devices": null}
    
   