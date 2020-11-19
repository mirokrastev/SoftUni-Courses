from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from accounts.common import get_user
from .common import get_likes, delete_image, GetPetMixin
from pets.models import Pet, Like
from pets.forms import PetCreateForm
from common.models import Comment
from common.forms import CommentForm


class AllPets(ListView):
    model = Pet
    template_name = 'pets/pet_list.html'
    context_object_name = 'pets'


class PetDetail(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pet = None
        self.comment_form = None

    def dispatch(self, request, *args, **kwargs):
        self.pet = Pet.objects.get(pk=kwargs['pk'])
        if self.request.user.pk != self.pet.pk:
            self.comment_form = CommentForm()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, pk, *args, **kwargs):
        likes_count = Like.objects.filter(pet_id=pk)
        comments = Comment.objects.filter(pet_id=pk)

        return {'pet': self.pet, 'comment_form': self.comment_form,
                'likes': len(likes_count), 'comments': comments}

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(self.pet.pk)
        return render(self.request, 'pets/pet_detail.html', context)

    def post(self, request, *args, **kwargs):
        if self.request.user.pk == self.pet.user.pk:
            return Http404

        Comment.objects.create(pet=self.pet, user=get_user(self.request.user.pk),
                               comment=self.request.POST['comment'])
        return self.get(request, *args, **kwargs)


class PetLike(View):
    def dispatch(self, request, *args, **kwargs):
        if self.request.method != 'POST':
            raise Http404
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, pk):
        pet = Pet.objects.get(pk=pk)
        user = get_user(self.request.user.pk)
        like = get_likes(user, pet)

        if like or pet.user.pk == user.pk:
            return Http404

        Like.objects.create(pet=pet, user=user)
        return redirect('pet_detail', pk=pk)


class PetCreate(CreateView):
    form_class = PetCreateForm
    template_name = 'pets/pet_create.html'
    context_object_name = 'form'

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = get_user(self.request.user.pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('all_pets')


class PetEdit(GetPetMixin, UpdateView):
    template_name = 'pets/pet_edit.html'
    context_object_name = 'form'
    form_class = PetCreateForm

    def form_valid(self, form):
        if self.request.FILES:
            delete_image(self.obj.image_field.path)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('pet_detail', kwargs={'pk': self.kwargs['pk']})


class PetDelete(GetPetMixin, DeleteView):
    template_name = 'pets/pet_delete.html'

    def delete(self, request, *args, **kwargs):
        delete_image(self.obj.image_field.path)
        return super().delete(self, request, *args, **kwargs)

    def get_success_url(self):
        return reverse('all_pets')
