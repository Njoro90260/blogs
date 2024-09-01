from django.shortcuts import render, redirect
# Create your views here.

def index(request):
    """The home page for blogs."""
    return render(request, 'blogs/index.html')
