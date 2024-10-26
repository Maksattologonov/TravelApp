from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .services import subscribe_to_user, subscribe_to_country, subscribe_to_tag
from accounts.models import User
from countries.models import Country
from posts.models import Tag


@login_required
def subscribe_user(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    subscribe_to_user(request.user, target_user)
    return redirect('users:user_detail', user_id=user_id)


@login_required
def subscribe_country(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    subscribe_to_country(request.user, country)
    return redirect('countries:country_detail', country_id=country_id)


@login_required
def subscribe_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    subscribe_to_tag(request.user, tag)
    return redirect('posts:tag_detail', tag_id=tag_id)
