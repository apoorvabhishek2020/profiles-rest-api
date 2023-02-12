"""
This module defines all the urls mappings for profiles_api app.
"""
from django.urls import path

from profiles_api import views

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view(), name="hello-view"),
]
