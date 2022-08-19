from django.shortcuts import render
from utils.recipes.factory import make_recipe


# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', {
        'recipes': [make_recipe() for _ in range(6)],
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', {
        'recipe': make_recipe(),
    })
