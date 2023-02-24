======================
django CMS Bootstrap 5
======================

This project is not associated with django CMS 

|pypi| |build| |coverage|

**django CMS Site Importer** is an addon bundle for django CMS that adds commaands to manage.py allowing
static html sites to be imported into Django CMS.

Installation
------------

For a manual install:

* Clone the repository into your django cms application folder as another app.
* (Future alternative) run ``pip install djangocms-site-importer``
* add the following entries to your ``INSTALLED_APPS``::

    'djangocms-site-importer',

You will then be able to import a site using::

    python manage.py import-site path_to_site_dir