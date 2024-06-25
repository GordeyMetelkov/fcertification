from ...models import Recipe
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "add image"

    def handle(self, *args, **kwargs):
        recipes = Recipe.objects.filter().all()
        for recipe in recipes:
            recipe.image = './recipe-img.png'
            recipe.save()