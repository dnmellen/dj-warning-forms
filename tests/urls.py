# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.urls import path
from django.contrib import admin
from example.views import PollCreateView, PollListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("list/", PollListView.as_view(), name="list"),
    path("", PollCreateView.as_view(), name="create"),
]
