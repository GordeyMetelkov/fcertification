from django import forms
from .models import Category


class RecipeForm(forms.Form):
    name = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea)
    cooking_steps = forms.CharField(widget=forms.Textarea, required=True)
    cooking_time_hours = forms.IntegerField(min_value=0, max_value=23, initial=1)
    cooking_time_minutes = forms.IntegerField(min_value=0, max_value=59, initial=0)
    author = forms.CharField(initial='Гость')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
    image = forms.ImageField()
