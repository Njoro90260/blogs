from django.shortcuts import render, redirect
from .models import BlogPost
from django.urls import reverse
from .forms import BlogForm
from django.urls import reverse 
# Create your views here.

def index(request):
    """The home page for blogs."""
    return render(request, 'blogs/index.html')

def blogs(request):
    """Page for the blogs."""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blogpost(request, title_id):
    """Page for the blogpost."""
    blogpost = BlogPost.objects.get(id=title_id)
    context = {'blogpost': blogpost}
    return render(request, 'blogs/blogpost.html', context)

def newblog(request):
    """Page for adding a new blog."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogForm()
    else:
        # POST data submitted; process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save() #get new blogpost instance.
            return redirect(reverse('blogs:blogpost', args=[new_blog.id])) 
    
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)




