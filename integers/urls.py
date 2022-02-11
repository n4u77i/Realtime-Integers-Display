import imp
from django import views
from django.urls import path

from . import views

app_name = 'integers'

urlpatterns = [
    path('', views.index, name='index'),
]
