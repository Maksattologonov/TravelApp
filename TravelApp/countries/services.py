from .models import Country


def get_country_list():
    return Country.objects.filter(posts__isnull=False).distinct()
