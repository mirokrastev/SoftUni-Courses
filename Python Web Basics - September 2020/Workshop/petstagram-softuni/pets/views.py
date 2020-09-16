from django.shortcuts import render, redirect
from pets.models import Pet, Like
from pets.forms import PetCreateForm
from common.models import Comment
from common.forms import CommentForm


def pet_all(request):
    all_pets = Pet.objects.all()
    return render(request, 'pets/pet_list.html', {'pets': all_pets})


def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        Comment.objects.create(pet=pet, comment=request.POST['comment'])

    likes_count = Like.objects.filter(pet_id=pk)
    comment_form = CommentForm()
    comments = Comment.objects.filter(pet_id=pk)

    content = {'pet': pet, 'likes': len(likes_count),
               'comments': comments, 'comment_form': comment_form}

    return render(request, 'pets/pet_detail.html', content)


def pet_like(request, pk):
    pet = Pet.objects.get(pk=pk)
    Like.objects.create(pet=pet)
    return redirect('pet_detail', pk=pk)


def pet_create(request):
    form = PetCreateForm()
    if request.method == 'POST':
        form.__init__(request.POST)
        if form.is_valid():
            form.save()
        return redirect('all_pets')
    return render(request, 'pets/pet_create.html', {'form': form})


def pet_edit(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        form = PetCreateForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_detail', pk)
    form = PetCreateForm(instance=pet)
    return render(request, 'pets/pet_edit.html', {'form': form})


def pet_delete(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('all_pets')
    return render(request, 'pets/pet_delete.html')
