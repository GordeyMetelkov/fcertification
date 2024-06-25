from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.DurationField()
    author = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    image = models.ImageField(default='')


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
