from django.shortcuts import render, redirect
from .models import BlogPost
# Create your views here.

def index(request):
    """The home page for blogs."""
    return render(request, 'blogs/index.html')

def blogs(request):
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)
