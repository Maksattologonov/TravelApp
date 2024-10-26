from django.contrib import admin
from .models import Post, Comment, Tag, PostImage, PostRating, PostLiftLog


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'country', 'created_at', 'is_active')
    list_filter = ('country', 'is_active')
    search_fields = ('title', 'author__username', 'country__name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('author__username', 'post__title')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')


@admin.register(PostRating)
class PostRatingAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'rating')


@admin.register(PostLiftLog)
class PostLiftLogAdmin(admin.ModelAdmin):
    list_display = ('post', 'lifted_at', 'lift_until', 'lift_days_of_week')
