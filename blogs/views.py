from django.shortcuts import render, redirect
from .models import BlogPost
from django.urls import reverse
# Create your views here.

def index(request):
    """The home page for blogs."""
    return render(request, 'blogs/index.html')

def blogs(request):
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blogpost(request, title_id):
    blogpost = BlogPost.objects.get(id=title_id)
    context = {'blogpost': blogpost}
    return render(request, 'blogs/blogpost.html', context)


