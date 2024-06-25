import datetime
import random

from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Recipe, Category, RecipeCategory
from .forms import RecipeForm


def index(request):
    title = 'Главная'
    all_recipes = Recipe.objects.filter().all()
    recipes = []
    for _ in range(5):
        check = True
        while check == True:
            recipe = random.choice(all_recipes)
            if recipe not in recipes:
                time = str(recipe.cooking_time).split('.')[0][:-3]
                recipe.cooking_time = time
                recipes.append(recipe)
                check = False
    return render(request, 'fs_app/index.html', {'recipes': recipes, 'title': title})


def recipe(request, recipe_id):
    title = 'Рецепт'
    recipe = Recipe.objects.filter(pk=recipe_id).first()
    time = str(recipe.cooking_time).split('.')[0][:-3]
    return render(request,
                  'fs_app/recipe.html',
                  {'recipe': recipe, 'time': time, 'title': title}
                  )


def category(request, category_name):
    category = Category.objects.filter(name=category_name).first()
    title = category_name
    recipes = Recipe.objects.filter(category=category.pk).all()
    return render(request, 'fs_app/category.html', {'recipes': recipes, 'title': title})


def categories(request):
    title = 'Категории'
    return render(request, 'fs_app/categories.html', {'title': title})


def add_recipe(request):
    title = 'Добавление рецепт'
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            new_recipe = Recipe(
                name=data['name'],
                description=data['description'],
                cooking_steps=data['cooking_steps'],
                cooking_time=datetime.timedelta(hours=data['cooking_time_hours'], minutes=data['cooking_time_minutes']),
                author=data['author'],
                category=data['category'],
                image=data['image'],
            )
            new_recipe.save()
            fs = FileSystemStorage()
            fs.save(new_recipe.image.name, new_recipe.image)
            return redirect('recipe', new_recipe.pk)
    else:
        form = RecipeForm()
    return render(
        request,
        'fs_app/add_recipe.html',
        {'form': form, 'title': title}
    )

def logout_view(request):
    logout(request)
    return redirect('login')

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def about(request):
    title = 'Обо мне'
    return render(request, 'fs_app/about.html', {'title': title})

