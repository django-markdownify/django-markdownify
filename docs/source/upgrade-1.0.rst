Upgrade guide to 1.0
====================

Package name
------------

To prevent conflicts with `python-markdownify
<https://github.com/matthewwithanm/python-markdownify>`_, this package module
was renamed from ``markdownify`` to ``django_markdownify``.

Rename the settings ``INSTALLED_APPS`` entry from ``markdownify`` to
``django_markdownify``.

To ease the migration process, the template tag library name remain
``markdownify``, and should not cause conflicts, as it is specific to Django.
