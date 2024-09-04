"""Defines url patterns for blogs."""
from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #path to view all the blogs
    path('blogs/', views.blogs, name="blogs"),
    #path to a specific blog
    path('blog-view/<int:title_id>', views.blogpost, name="blogpost"),
    # path to add a new blog.
    path('new-blog/', views.newblog, name="newblog"),
]