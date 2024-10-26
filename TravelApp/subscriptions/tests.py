from django.test import TestCase
from django.urls import reverse
from accounts.models import User
from countries.models import Country
from posts.models import Tag


class SubscriptionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.another_user = User.objects.create_user(username="otheruser", password="otherpass")
        self.country = Country.objects.create(name="Test Country")
        self.tag = Tag.objects.create(name="Test Tag")
        self.client.login(username="testuser", password="testpass")

    def test_user_subscription(self):
        response = self.client.get(reverse('subscriptions:subscribe_user', args=[self.another_user.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.user.subscriptions.filter(subscribed_to=self.another_user).exists())

    def test_country_subscription(self):
        response = self.client.get(reverse('subscriptions:subscribe_country', args=[self.country.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.user.countrysubscription_set.filter(country=self.country).exists())

    def test_tag_subscription(self):
        response = self.client.get(reverse('subscriptions:subscribe_tag', args=[self.tag.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.user.tagsubscription_set.filter(tag=self.tag).exists())
