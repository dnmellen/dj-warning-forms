#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dj-warning-forms
------------

Tests for `dj-warning-forms` models module.
"""

from django.http.request import QueryDict
from django.test import TestCase
from example.forms import PollForm


class TestDjangoWarningForms(TestCase):
    def test_render_warning_form_ok(self):
        form = PollForm(data=QueryDict("question=What is your favorite color?"))
        self.assertTrue(form.is_valid())
        self.assertFalse(form.cleaned_data["ignore_warnings"])
        self.assertEqual(form.errors, {})
        self.assertEqual(form.warnings, [])

    def test_render_warning_form_warning(self):
        form = PollForm(data=QueryDict("question=What is your favorite color"))
        self.assertFalse(form.is_valid())
        self.assertTrue(form.data.get("ignore_warnings"))
        self.assertEqual(form.errors, {})
        warning_dict = {
            "field": "question",
            "message": "Weird question",
            "description": "This question does not end with a question mark. Are you sure you want to publish this question?",  # noqa
        }
        self.assertIn(
            warning_dict,
            form.warnings,
        )
