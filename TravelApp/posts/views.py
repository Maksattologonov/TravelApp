from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .services import get_posts_for_user, get_post_comments, add_post_rating, paginate_posts
from django.contrib import messages


@login_required
def post_list(request):
    posts = get_posts_for_user(request.user)
    page_number = request.GET.get('page', 1)
    page_obj = paginate_posts(posts, page_number)
    return render(request, 'posts/post_list.html', {'page_obj': page_obj})


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = get_post_comments(post)
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments})


@login_required
def post_rate(request, post_id, rating):
    post = get_object_or_404(Post, id=post_id)
    add_post_rating(post, request.user, rating)
    messages.success(request, 'You have successfully rated the post!')
    return redirect('posts:post_detail', post_id=post.id)
