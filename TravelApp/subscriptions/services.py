from .models import UserSubscription, CountrySubscription, TagSubscription


def subscribe_to_user(user, target_user):
    UserSubscription.objects.get_or_create(subscriber=user, subscribed_to=target_user)


def subscribe_to_country(user, country):
    CountrySubscription.objects.get_or_create(user=user, country=country)


def subscribe_to_tag(user, tag):
    TagSubscription.objects.get_or_create(user=user, tag=tag)
