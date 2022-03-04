from django.forms import ModelForm
from dj_warning_forms.forms import WarningFormMixin, FormFieldWarning

from .models import Poll


class PollForm(WarningFormMixin, ModelForm):
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
