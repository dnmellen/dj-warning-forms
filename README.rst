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

.. image:: https://github.com/dnmellen/dj-warning-forms/blob/master/docs/demo.gif?raw=true

Documentation
-------------

The full documentation is at https://dj-warning-forms.readthedocs.io.

Quickstart
----------

Install Django Warning Forms::

    pip install dj-warning-forms

Use the form mixin in any form
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from django import forms
    from dj_warning_forms.forms import WarningFormMixin, FormFieldWarning

    from .models import Poll


    class PollForm(WarningFormMixin, forms.ModelForm):
        question = forms.CharField(
            max_length=200, widget=forms.TextInput(attrs={"autocomplete": "off"})
        )

        class Meta:
            model = Poll
            fields = "__all__"

        def warning_question(self) -> List[FormFieldWarning]:
            if not self.cleaned_data["question"].endswith("?"):
                return [
                    FormFieldWarning(
                        message="Weird question",
                        description="This question does not end with a question mark. Are you sure you want to publish this question?",  # noqa
                    )
                ]
            return []

Adding a warning is as simple as adding a method with the ``warning_`` prefix. This method must return a
list of FormFieldWarning objects.

Showing warnings in the template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can find the list of warnings in ``form.warnings``.

.. code-block:: html

    {% block content %}
    <form action="." method="post">
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="Submit">

        <!-- Customize your form warnings as you wish -->
        {% if form.warnings %}
            <div class="rounded p-2 mt-2 bg-warning">
                <ul>
                {% for warning in form.warnings %}
                    <li><b>{{ warning.message }}:</b> {{ warning.description }}</li>
                {% endfor %}
                </ul>
            </div>
        {% endif %}
        <!-- End of form warnings -->
    </form>
    {% endblock %}


Features
--------

- No external dependencies
- Minimal changes needed in your forms
- Easy to customize

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
