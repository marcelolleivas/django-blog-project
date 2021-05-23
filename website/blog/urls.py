from django.urls import path

from . import views

urlpatterns = [
    path("", views.BlogListView.as_view(), name="home"),
    path(
        "post/<slug:slug>/", views.BlogDetailsView.as_view(), name="post_detail"
    ),
]
