from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
from .models import Post, Comment
from django.views.generic import ListView, DetailView, View
from .forms import CommentForm

# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self) -> QuerySet[Any]:
        query_set = super().get_queryset()
        data = query_set[:3]
        return data
    
class AllPostsView(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]

class SinglePostView(DetailView):
    template_name = "blog/post_detail.html"
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        context["comments"] = self.object.comments.all()
        return context
    
class SingleCommentView(DetailView):
    template_name = "blog/post_comment_detail.html"
    model = Comment
    context_object_name = "comment"


# def index(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })

# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request, "blog/all_posts.html", {
#         "posts": all_posts
#     })

# def post_by_name(request, slug):
#     selected_post = Post.objects.get(slug=slug)
#     return render(request, "blog/post_detail.html", {
#         "post": selected_post
#     })


def add_comment(request, post_slug):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    rating = request.POST["rating"]
    text = request.POST["text"]
    selected_post = Post.objects.get(slug=post_slug)
    new_comment = Comment(first_name=first_name, last_name=last_name, rating=rating, text=text)
    new_comment.save()
    selected_post.comments.add(new_comment)
    selected_post.save()
    return HttpResponseRedirect(f"/posts/{selected_post.slug}")


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts", None)
        if not stored_posts:
            stored_posts = []
        return render(request, "blog/stored_posts.html", {
            "stored_posts": stored_posts
        })
    
    def post(self, request):
        post_slug = request.POST['post_slug']
        is_remove = request.POST.get("is_remove", "False")
        stored_posts = request.session.get("stored_posts", None)
        if not stored_posts:
            stored_posts = []
        if post_slug not in stored_posts and is_remove == "False":
            stored_posts.append(post_slug)
            request.session["stored_posts"] = stored_posts
        elif post_slug in stored_posts and is_remove == "True":
            stored_posts.remove(post_slug)
            request.session["stored_posts"] = stored_posts

        if is_remove == "True":
            return HttpResponseRedirect("/read_later/")
        return HttpResponseRedirect(f"/posts/")