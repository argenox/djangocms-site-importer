from django.core.management.base import BaseCommand, CommandError
from djangocms_site_importer.management.core.SiteParser import *
#from cms.api import *

class Command(BaseCommand):
    help = 'Imports the site'

    def add_arguments(self, parser):
        parser.add_argument('html_dir', nargs='+', type=str)

    def handle(self, *args, **options):
        print("Running Site Import")

        path = options['html_dir'][0]
        print("Selected path " + path)

        sp = SiteParser(path)

        print("Parsing " + sp.html_dir)

        sp.parseDir()

        for page in sp.page_list:
            #my_pagecreate_page("Test", "templates/bootstrap5.html", "en")
            from cms.api import create_page, add_plugin
            new_page = create_page(page.title, language='en', template='bootstrap5.html')

            # Get root placeholder
            placeholder = page.placeholders.get(slot='body')

            for item in page.parse_tree:
                add_plugin(placeholder, 'TextPlugin', 'en', body='hello world')

    
        #    add_plugin(placeholder, plugin_type, language, position='last-child', target=None, **data)
        

        