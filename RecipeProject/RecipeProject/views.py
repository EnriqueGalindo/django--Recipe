from django.shortcuts import render
from .models import Author, Recipe


def index(request):
    return render(request,
                  'RecipeProject/index.html',
                  {'recipes': Recipe.objects.all()}
                  )


def author(request, author):
    return render(request,
                  'RecipeProject/author.html',
                  {'authors': Author.objects.get(name=author),
                   'recipes': Recipe.objects.filter(author__name=author)
                   }
                  )


def detail(request, recipe):
    return render(request,
                  'RecipeProject/detail.html',
                  {'recipes': Recipe.objects.get(title=recipe)}
                  )
