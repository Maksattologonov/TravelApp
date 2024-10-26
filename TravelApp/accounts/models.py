from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    AUTHORIZED_USER = 'user', 'Authorized User'
    GUEST = 'guest', 'Guest'


class User(AbstractUser):
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.GUEST)
    can_post = models.BooleanField(default=True)
    is_banned = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.username
