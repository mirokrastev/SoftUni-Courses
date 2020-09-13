from django.shortcuts import render, redirect
from pets.models import Pet, Like


def pet_all(request):
    all_pets = Pet.objects.all()
    return render(request, 'pets/pet_list.html', {'pets': all_pets})


def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    likes_count = Like.objects.filter(pet_id=pk)
    return render(request, 'pets/pet_detail.html', {'pet': pet, 'likes': len(likes_count)})


def pet_like(request, pk):
    pet = Pet.objects.get(pk=pk)
    Like.objects.create(pet=pet)
    return redirect('pet_detail', pk=pk)
