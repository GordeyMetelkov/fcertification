from ...models import Category, Recipe, RecipeCategory
from django.core.management.base import BaseCommand
from random import choice, randint


class Command(BaseCommand):
    help = "Create new recipes"

    def handle(self, *args, **kwargs):
        for i in range(11, 21):
            recipe = Recipe(
                name=f'name{i}',
                description=f'Some decription about recipe',
                cooking_steps=f'1. step, 2. step, 3. step',
                cooking_time='1:20',
                author=f'author-{i}',
                category=Category.objects.filter(pk=randint(1,5)).first()
            )
            recipe.save()
