from django.core.management.base import BaseCommand, CommandError
from djangocms_site_importer.management.core.SiteParser import *

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

        