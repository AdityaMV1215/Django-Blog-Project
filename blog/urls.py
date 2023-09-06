from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="index"),
    path("read_later/", views.ReadLaterView.as_view(), name="read_later"),
    path("posts/", views.AllPostsView.as_view(), name="posts"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post_details"),
    path("posts/add_comment/<slug:post_slug>", views.add_comment, name="add_comment"),
    path("posts/comment/<int:pk>", views.SingleCommentView.as_view(), name="comment_details")
]
