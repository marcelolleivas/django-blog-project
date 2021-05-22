from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "blog/home.html"


class BlogDetailsView(BlogListView):
    model = Post
    template_name = 'blog/post_detail.html'
