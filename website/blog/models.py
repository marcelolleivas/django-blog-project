from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super(PublishedManager, self)
            .get_queryset()
            .filter(status="published_in")
        )


class Post(models.Model):
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

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])

    class Meta:
        ordering = ("-published_in",)

    def __str__(self):
        return f'{self.published}-{self.title}'
