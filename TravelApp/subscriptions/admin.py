from django.contrib import admin
from .models import UserSubscription, CountrySubscription, TagSubscription


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'subscribed_to')
    search_fields = ('subscriber__username', 'subscribed_to__username')


@admin.register(CountrySubscription)
class CountrySubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'country')
    search_fields = ('user__username', 'country__name')


@admin.register(TagSubscription)
class TagSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'tag')
    search_fields = ('user__username', 'tag__name')
