django-pipeline-forgiving
===========================================================

.. image:: https://badge.fury.io/py/django-pipeline-forgiving.png
    :target: https://badge.fury.io/py/django-pipeline-forgiving

.. image:: https://pypip.in/d/django-pipeline-forgiving/badge.png
    :target: https://pypi.python.org/pypi/django-pipeline-forgiving

An extension of the django-pipeline storage backend which forgives 
missing files.

This was created to solve the problem of using django-pipline with 
third-party Django apps which have missing files in their css.

For example, running ``collectstatic`` against an app using both 
``djangobb_forum`` and ``pipeline`` produced (at the time of writing)::

  $ django-admin.py collectstatic
  ...
  ValueError: The file 'djangobb_forum/themes/default/img/active_forum.gif' could not be found with <nest.apps.core.storages.PipelineCachedStorage object at 0x108d06090>.

Installation
------------

Installation using pip::

    pip install django-pipeline-forgiving

Usage
-----

Set in your settings.py::

    STATICFILES_STORAGE = 'django_pipeline_forgiving.storages.PipelineForgivingStorage'

Credits
-------

Written by `Adam Charnock`_.

``django-pipeline-forgiving`` is packaged using seed_.

.. _seed: https://github.com/adamcharnock/seed/
.. _Adam Charnock: https://github.com/adamcharnock/
