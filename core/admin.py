from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "created_in", "published_in", "status")
    list_display = ("title", "author", "published_in", "status")
    search_fields = ("title", "content")
    raw_id_fields = ("author",)
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_in"
