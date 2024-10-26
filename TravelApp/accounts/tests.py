from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountsTestCase(TestCase):
    def test_registration(self):
        response = self.client.post(reverse("accounts:register"), {
            "username": "newuser",
            "password1": "newpassword",
            "password2": "newpassword"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login(self):
        User.objects.create_user(username="testuser", password="testpass")
        response = self.client.post(reverse("accounts:login"), {
            "username": "testuser",
            "password": "testpass"
        })
        self.assertEqual(response.status_code, 302)
