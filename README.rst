=============================
Django Warning Forms
=============================

.. image:: https://badge.fury.io/py/dj-warning-forms.svg
    :target: https://badge.fury.io/py/dj-warning-forms

.. image:: https://travis-ci.org/dnmellen/dj-warning-forms.svg?branch=master
    :target: https://travis-ci.org/dnmellen/dj-warning-forms

.. image:: https://codecov.io/gh/dnmellen/dj-warning-forms/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dnmellen/dj-warning-forms

Add warnings to your Django Forms easily

Documentation
-------------

The full documentation is at https://dj-warning-forms.readthedocs.io.

Quickstart
----------

Install Django Warning Forms::

    pip install dj-warning-forms

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_warning_forms.apps.DjWarningFormsConfig',
        ...
    )

Add Django Warning Forms's URL patterns:

.. code-block:: python

    from dj_warning_forms import urls as dj_warning_forms_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_warning_forms_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
