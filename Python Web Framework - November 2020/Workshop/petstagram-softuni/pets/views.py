from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from accounts.common import get_user
from .common import get_likes, delete_image
from pets.models import Pet, Like
from pets.forms import PetCreateForm
from common.models import Comment
from common.forms import CommentForm


@login_required
def pet_all(request):
    all_pets = Pet.objects.all()
    return render(request, 'pets/pet_list.html', {'pets': all_pets})


@login_required
def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    comment_form = None
    if request.user.pk != pet.user.pk:
        comment_form = CommentForm()

    if request.method == 'POST':
        if request.user.pk == pet.user.pk:
            return Http404

        Comment.objects.create(pet=pet, user=get_user(request.user.pk), comment=request.POST['comment'])

    likes_count = Like.objects.filter(pet_id=pk)
    comments = Comment.objects.filter(pet_id=pk)

    context = {'pet': pet, 'likes': len(likes_count),
               'comments': comments, 'comment_form': comment_form}

    return render(request, 'pets/pet_detail.html', context)


@login_required
def pet_like(request, pk):
    if not request.method == 'POST':
        return Http404

    pet = Pet.objects.get(pk=pk)
    user = get_user(request.user.pk)
    like = get_likes(user, pet)

    if like or pet.user.pk == user.pk:
        return Http404

    Like.objects.create(pet=pet, user=user)
    return redirect('pet_detail', pk=pk)


@login_required
def pet_create(request):
    if request.method == 'POST':
        form = PetCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = get_user(request.user.pk)
            form.save()
            return redirect('all_pets')
    else:
        form = PetCreateForm()

    return render(request, 'pets/pet_create.html', {'form': form})


@login_required
def pet_edit(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.user.pk != pet.user.pk:
        return Http404

    if request.method == 'POST':
        form = PetCreateForm(request.POST, request.FILES, instance=pet)
        delete_image(pet.image_field.path)

        if form.is_valid():
            form.save()
            return redirect('pet_detail', pk)
    else:
        form = PetCreateForm(instance=pet)

    return render(request, 'pets/pet_edit.html', {'form': form})


@login_required
def pet_delete(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.user.pk != pet.user.pk:
        return Http404

    if request.method == 'GET':
        return render(request, 'pets/pet_delete.html')

    delete_image(pet.image_field.path)
    pet.delete()
    return redirect('all_pets')
