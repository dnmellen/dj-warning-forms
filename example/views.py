from typing import Any, Dict
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from .models import Poll
from .forms import PollForm


class PollCreateView(CreateView):
    model = Poll
    form_class = PollForm
    template_name = "example/create.html"
    success_url = reverse_lazy("list")

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        self.extra_context = {
            "title": "Create a new poll",
        }
        return super().get_context_data(**kwargs)


class PollListView(ListView):
    model = Poll
    template_name = "example/list.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        self.extra_context = {
            "title": "Existing polls",
        }
        return super().get_context_data(**kwargs)
