from django.contrib import admin
from django.urls import path, include
from .api import Api

urlpatterns = [
    path('all/', Api.as_view()),
    path('<pk>/', Api.as_view()),
]
