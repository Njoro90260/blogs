from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from django.urls import reverse
from .forms import BlogForm
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from django.http import Http404
# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# Create your views here

# @csrf_exempt
# def toggle_theme(request):
#     """View function to change the theme."""
#     if request.method == "POST":
#         data = json.loads(request.body)
#         theme = data.get('theme', 'light')
#         request.session['theme'] = theme
#         return JsonResponse({"status": "success", "theme": theme})
#     return JsonResponse({"status": "error"}, status=400)

def index(request):
    """The home page for blogs."""
    return render(request, 'blogs/index.html')

def blogs(request):
    """Page for the blogs."""
    blogs = BlogPost.objects.order_by('-date_added')
    logged_user = request.user
    context = {'blogs': blogs, 'logged_user': logged_user}
    return render(request, 'blogs/blogs.html', context)

def blogpost(request, title_id):
    """Page for the blogpost."""
    blogpost = get_object_or_404(BlogPost, id=title_id)
    logged_user = request.user
    # Make sure the blogpost belongs to the current user.
    context = {'blogpost': blogpost, 'logged_user': logged_user}
    return render(request, 'blogs/blogpost.html', context)

@login_required
def newblog(request):
    """Page for adding a new blog."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogForm()
    else:
        # POST data submitted; process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False) #get new blogpost instance.
            new_blog.owner = request.user
            new_blog.save()
            return redirect(reverse('blogs:blogpost', args=[new_blog.id])) 
    
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def editblog(request, blog_id):
    """View for editting the blog."""
    blog = get_object_or_404(BlogPost, id=blog_id)
    if blog.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry
        form = BlogForm(instance=blog)
    else:
        # Post data submitted; process data.
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogpost', title_id=blog.id)
        
    # show the editing workspace
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)

@login_required
def delete_blog(request ,id):
    """View to delete a blog post."""
    blogpost = get_object_or_404(BlogPost, id=id)
    if blogpost.owner != request.user:
        raise Http404

    if request.method == 'POST':
        blogpost.delete()
        return redirect(reverse('blogs:blogs'))
    
    context = {'blogpost': blogpost}
    return render(request, 'blogs/confirm_delete.html', context)