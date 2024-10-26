from .models import Post, Comment, PostRating
from django.core.paginator import Paginator
from django.db.models import Q


def get_posts_for_user(user):
    followed_users = user.subscriptions.values_list('subscribed_to', flat=True)
    followed_countries = user.countrysubscription_set.values_list('country', flat=True)
    followed_tags = user.tagsubscription_set.values_list('tag', flat=True)

    return Post.objects.filter(
        Q(author__id__in=followed_users) |
        Q(country__id__in=followed_countries) |
        Q(tags__id__in=followed_tags)
    ).distinct().order_by('-created_at')


def get_post_comments(post):
    return post.comments.order_by('-created_at')


def add_post_rating(post, user, rating_value):
    rating, created = PostRating.objects.update_or_create(
        post=post, user=user, defaults={'rating': rating_value}
    )
    return rating


def paginate_posts(posts, page_number, per_page=10):
    paginator = Paginator(posts, per_page)
    return paginator.get_page(page_number)
