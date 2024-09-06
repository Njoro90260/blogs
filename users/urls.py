"""Defines urls patterns for users"""
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name='register'),
]