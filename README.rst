======================
django CMS Bootstrap 5
======================

This project is not associated with django CMS 

|pypi| |build| |coverage|

**django CMS Site Importer** is an addon bundle for django CMS that adds commaands to manage.py allowing
static html sites to be imported into Django CMS.

Why?
------------

Most of us probably are starting from something. Typically another site or front end pages that are developed.
Why take all that time and create all the pages manually? Just use this plugin and get your pages created for you.

How it Works
------------
django-cms site importer will go through the provided html directroy and create a page for each page
it finds. For pages that contain images, it will automatically try and locate the image, upload it
via django-filer used by django-cms, and properly update the image plugin.


Installation
------------

For a manual install:

* Clone the repository into your django cms application folder as another app.
* (Future alternative) run ``pip install djangocms-site-importer``
* add the following entries to your ``INSTALLED_APPS``::

    'djangocms-site-importer',

You will then be able to import a site using::

    python manage.py import-site path_to_site_dir