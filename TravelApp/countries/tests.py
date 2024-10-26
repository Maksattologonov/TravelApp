from django.test import TestCase
from django.urls import reverse
from .models import Country


class CountryViewTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="Test Country")

    def test_country_list_view(self):
        response = self.client.get(reverse('countries:country_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Country")

    def test_country_detail_view(self):
        response = self.client.get(reverse('countries:country_detail', args=[self.country.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Country")
