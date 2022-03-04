from collections import namedtuple
import inspect
from django import forms


FormFieldWarning = namedtuple("FormFieldWarning", ["message", "description"])


class WarningFormMixin:
    """Classes using WarningFormMixin should implement methods to catch warnings

    >>> def warning_mailboxes(self) -> List[FormFieldWarning]:
        if some condition:
            return FormFieldWarning(message, description)
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["ignore_warnings"] = forms.BooleanField(
            required=False, initial=False, widget=forms.HiddenInput()
        )
        self.warnings = []

    def get_warnings(self):
        if self.cleaned_data.get("ignore_warnings"):
            return []
        else:
            warning_methods = [
                (method_name, method)
                for method_name, method in inspect.getmembers(
                    self, predicate=inspect.ismethod
                )
                if method_name.startswith("warning_")
            ]
            for method_name, method in warning_methods:
                warnings = method()
                if warnings:
                    self.warnings.extend(
                        [
                            {
                                "field": method_name.split("warning_")[1],
                                "message": warning.message,
                                "description": warning.description,
                            }
                            for warning in warnings
                        ]
                    )
            self.data._mutable = True
            self.data["ignore_warnings"] = True
            self.data._mutable = False
            return self.warnings

    def is_valid(self):
        return super().is_valid() and not self.get_warnings()
