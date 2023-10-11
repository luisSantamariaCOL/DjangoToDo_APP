from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'todo'
urlpatterns = [
    path('addTask/', views.add_task, name='addTask'),
]