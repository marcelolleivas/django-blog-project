from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .models import Post

"""
STATUS = (("draft", "Draft"), ("published", "Published"))
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_in = models.DateTimeField(default=timezone.now())
    created_in = models.DateTimeField(auto_now_add=True)
    changed_in = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default="draft")
    objects = models.Manager()
    published = PublishedManager()
"""


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
