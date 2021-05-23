from django.views.generic import DetailView, ListView

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "blog/home.html"


class BlogDetailsView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
