import django.contrib.auth
from django.urls import path
from . import views
from .models import Recipe

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<int:recipe_id>/', views.recipe, name='recipe'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('categories/', views.categories, name='categories'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("about/", views.about, name="about"),
]