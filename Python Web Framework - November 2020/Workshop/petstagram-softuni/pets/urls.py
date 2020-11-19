from django.contrib.auth.decorators import login_required
from django.urls import path
from pets import views

urlpatterns = [
    path('', login_required(views.AllPets.as_view()), name='all_pets'),
    path('create', login_required(views.PetCreate.as_view()), name='pet_create'),
    path('details/<int:pk>', login_required(views.PetDetail.as_view()), name='pet_detail'),
    path('like/<int:pk>', login_required(views.PetLike.as_view()), name='pet_like'),
    path('edit/<int:pk>', login_required(views.PetEdit.as_view()), name='pet_edit'),
    path('delete/<int:pk>', login_required(views.PetDelete.as_view()), name='pet_delete'),
]
