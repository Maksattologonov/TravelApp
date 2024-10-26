from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, Comment, PostRating
from countries.models import Country
from django.urls import reverse

User = get_user_model()


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.country = Country.objects.create(name="Test Country")
        self.post = Post.objects.create(
            author=self.user, country=self.country, title="Test Post", content="This is a test post"
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.author.username, "testuser")

    def test_comment_creation(self):
        comment = Comment.objects.create(post=self.post, author=self.user, content="Test Comment")
        self.assertEqual(comment.content, "Test Comment")
        self.assertEqual(comment.post, self.post)


class PostRatingTest(TestCase):
    def test_post_rating(self):
        # Тестируем добавление рейтинга
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse('posts:post_rate', args=[self.post.id, 1]))  # +1 к рейтингу
        self.assertEqual(response.status_code, 302)
        rating = PostRating.objects.get(post=self.post, user=self.user)
        self.assertEqual(rating.rating, 1)
