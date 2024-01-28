from django.contrib import admin
from django.urls import path, include
from .views import myview, edit, delete

urlpatterns = [
    path('', myview),
    path('edit/<pk>/', edit, name="editROW"),
    path('delete/<pk>/', delete, name="deleteROW"),
]
