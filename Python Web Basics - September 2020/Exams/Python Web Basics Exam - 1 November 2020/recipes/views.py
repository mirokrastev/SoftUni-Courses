from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeModelForm


def index(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeModelForm()

    context = {'form': form}
    return render(request, 'recipe/create.html', context)


def edit_recipe(request, id):
    recipe_obj = Recipe.objects.get(pk=id)

    if request.method == 'POST':
        form = RecipeModelForm(request.POST, instance=recipe_obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeModelForm(instance=recipe_obj)

    context = {'form': form}
    return render(request, 'recipe/edit.html', context)


def delete_recipe(request, id):
    recipe_obj = Recipe.objects.get(pk=id)
    if request.method == 'POST':
        recipe_obj.delete()
        return redirect('home')

    form = RecipeModelForm(instance=recipe_obj)

    for key in form.fields.keys():
        form.fields[key].widget.attrs.update({'disabled': ""})

    context = {'form': form}
    return render(request, 'recipe/delete.html', context)


def detail_recipe(request, id):
    recipe_obj = Recipe.objects.get(pk=id)

    form = RecipeModelForm(instance=recipe_obj)
    ingredients_ll = form['ingredients'].value().split(', ')

    context = {'form': form, 'obj': recipe_obj, 'ingredients': ingredients_ll}

    return render(request, 'recipe/details.html', context)
