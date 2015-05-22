=====
BCF Announcements
=====

bcf-announcements is a Django app for site-wide and user-targetted announcements.

Quick start
-----------

1. Add 'bcf-announcements' to your INSTALLED_APPS setting::

    INSTALLED_APPS = (
        ...
        'bcf-announcements',
    )

2. Include the bcf-announcements URLconf in your project urls.py::

    url(r'', include('bcf-announcements.urls')),
