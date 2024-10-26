from django.shortcuts import render, get_object_or_404
from .models import Country
from .services import get_country_list
from posts.services import paginate_posts


def country_list(request):
    countries = get_country_list()
    return render(request, 'countries/country_list.html', {'countries': countries})


def country_detail(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    posts = country.posts.order_by('-created_at')
    page_number = request.GET.get('page', 1)
    page_obj = paginate_posts(posts, page_number)
    return render(request, 'countries/country_detail.html', {'country': country, 'page_obj': page_obj})
