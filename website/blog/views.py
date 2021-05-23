from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView

from .models import Post


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_edit.html"
    fields = ["title", "slug", "content"]


class BlogCreateView(CreateView):
    model = Post
    template_name = "blog/post_new.html"
    fields = ["title", "slug", "content", "author"]


class BlogDetailsView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class BlogListView(ListView):
    model = Post
    template_name = "blog/home.html"
