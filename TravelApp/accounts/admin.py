from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'can_post', 'is_banned')
    list_filter = ('role', 'is_banned')
    search_fields = ('username', 'email')
