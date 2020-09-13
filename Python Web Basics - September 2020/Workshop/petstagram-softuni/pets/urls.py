from django.urls import path
from pets.views import pet_all, pet_detail, pet_like

urlpatterns = [
    path('', pet_all, name='all_pets'),
    path('details/<int:pk>', pet_detail, name='pet_detail'),
    path('like/<int:pk>', pet_like, name='pet_like')
]
