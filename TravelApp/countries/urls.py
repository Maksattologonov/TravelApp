from django.urls import path
from . import views

app_name = 'countries'

urlpatterns = [
    path('', views.country_list, name='country_list'),
    path('<int:country_id>/', views.country_detail, name='country_detail'),
]
