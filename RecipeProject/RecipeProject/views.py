from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .models import Author, Recipe
from .forms import RecipeAddForm, AuthorAddForm, RegisterForm, LoginForm, RecipeEditForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,
                  'index.html',
                  {'recipes': Recipe.objects.all()}
                  )


def author(request, id):
    author = Author.objects.get(id=id)
    recipes = Recipe.objects.filter(author=author)
    return render(request, "author.html", {"recipes": recipes, "author":author})


def detail(request, id):
    recipes = Recipe.objects.get(id=id)
    author = Author.objects.filter(name=request.user)
    if author == recipes.author:
        logged_user = True
    else:
        logged_user = False
    return render(request,
                  "detail.html", {
                                  "recipes": recipes,
                                  "logged_user": logged_user
                                  })


@login_required()
def add_recipe_view(request):
    html = "genericForm.html"

    if request.method == "POST":
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data["title"],
                author=data["author"],
                description=data["description"],
                time_required=data["time_required"],
                instructions=data["instructions"]
                )
            return redirect(reverse("home"))
    form = RecipeAddForm()
    return render(request, html, {'form': form})


def add_author_view(request):
    html = "genericForm.html"

    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data["name"],
                bio=data["bio"]
            )
            return redirect(reverse("home"))
    form = AuthorAddForm()

    return render(request, html, {'form': form})


def register_view(request):
    html = "genericForm.html"

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data["username"],
                password=data["password"]
            )
            Author.objects.create(
                name=data["name"],
                bio=data["bio"],
                user=user
            )
            login(request, user)
            return redirect(reverse("home"))

    form = RegisterForm()

    return render(request, html, {'form': form})


def edit_recipe_view(request, id):
    html = "editRecipe.html"
    if request.method == "POST":
        form = RecipeEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipeToUpdate = Recipe.objects.get(id=id)
            recipeToUpdate.title = data['title']
            recipeToUpdate.author = data['author']
            recipeToUpdate.description = data['description']
            recipeToUpdate.time_required = data['time_required']
            recipeToUpdate.instructions = data['instructions']
            recipeToUpdate.save()
    current_value = Recipe.objects.get(id=id)
    form = RecipeEditForm(initial={
        'title': current_value.title,
        'author': current_value.author,
        'description': current_value.description,
        'time_required': current_value.time_required,
        'instructions': current_value.instructions
    })
    return render(request, html, {'form': form})


def add_favorite_view(request, id):
    current_user = Author.objects.get(name=request.user)
    recipe_to_favorite = Recipe.objects.get(id=id)
    current_user.favorites.add(recipe_to_favorite)
    current_user.save()
    return HttpResponseRedirect(reverse('home'))


def favorites_view(request, id):
    current_user = Author.objects.get(id=id)
    return render(request, 'favorites.html',
                  {"favorites": current_user.favorites.all()})


def login_view(request):
    html = "genericForm.html"

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data["username"],
                password=data["password"])
            if user:
                login(request, user)
                return redirect(request.GET.get("next", "/"))
            else:
                return HttpResponse("invalid authentication")

    form = LoginForm()

    return render(request, html, {'form': form})


def logut_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
