from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView

from .models import Post


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "core/post_delete.html"
    success_url = reverse_lazy("home")


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "core/post_edit.html"
    fields = ["title", "content"]


class BlogCreateView(CreateView):
    model = Post
    template_name = "core/post_new.html"
    fields = ["title", "content", "author"]


class BlogDetailsView(DetailView):
    model = Post
    template_name = "core/post_detail.html"


class BlogListView(ListView):
    model = Post
    template_name = "core/home.html"
