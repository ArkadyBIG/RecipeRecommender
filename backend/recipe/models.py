from django.contrib.auth.models import User
from django.db import models

from ingredient.models import Ingredient


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
