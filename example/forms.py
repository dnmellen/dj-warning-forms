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

    def warning_question(self):
        if not self.cleaned_data["question"].endswith("?"):
            return [
                FormFieldWarning(
                    message="Weird question",
                    description="This question does not end with a question mark. Are you sure you want to publish this question?",  # noqa
                )
            ]
        return []


class PollNoWarningsForm(WarningFormMixin, forms.ModelForm):
    question = forms.CharField(
        max_length=200, widget=forms.TextInput(attrs={"autocomplete": "off"})
    )

    class Meta:
        model = Poll
        fields = "__all__"
