from django.urls import path
from pets.views import pet_all, pet_detail, pet_like, pet_create, pet_edit, pet_delete

urlpatterns = [
    path('', pet_all, name='all_pets'),
    path('create', pet_create, name='pet_create'),
    path('details/<int:pk>', pet_detail, name='pet_detail'),
    path('like/<int:pk>', pet_like, name='pet_like'),
    path('edit/<int:pk>', pet_edit, name='pet_edit'),
    path('delete/<int:pk>', pet_delete, name='pet_delete'),
]
