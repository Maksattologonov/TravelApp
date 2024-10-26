from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)  # Данные из API

    def __str__(self):
        return self.name
