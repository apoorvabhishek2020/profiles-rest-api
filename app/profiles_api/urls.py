"""
This module defines all the urls mappings for profiles_api app.
"""
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view(), name="hello-view"),
    path('', include(router.urls)),
]
