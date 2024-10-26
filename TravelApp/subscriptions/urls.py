from django.urls import path
from . import views

app_name = 'subscriptions'

urlpatterns = [
    path('user/<int:user_id>/', views.subscribe_user, name='subscribe_user'),
    path('country/<int:country_id>/', views.subscribe_country, name='subscribe_country'),
    path('tag/<int:tag_id>/', views.subscribe_tag, name='subscribe_tag'),
]
