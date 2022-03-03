=====
Usage
=====

To use Django Warning Forms in a project, add it to your `INSTALLED_APPS`:

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
