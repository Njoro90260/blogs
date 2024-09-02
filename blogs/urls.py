"""Defines url patterns for blogs."""
from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name="blogs"),
]