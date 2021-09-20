from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('createperson/', views.person_list, name='person_list'),
]
