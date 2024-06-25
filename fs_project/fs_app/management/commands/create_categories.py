from ...models import Category
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create new categories"

    def handle(self, *args, **kwargs):
        categories = ['Первые блюда', 'Вторые блюда', 'Выпечка', 'Десерты']
        for item in categories:
            category = Category(name=item)
            category.save()
