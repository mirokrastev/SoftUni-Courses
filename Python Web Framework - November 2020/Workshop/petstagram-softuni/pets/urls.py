from django.urls import path
from pets import views

urlpatterns = [
    path('', views.pet_all, name='all_pets'),
    path('create', views.pet_create, name='pet_create'),
    path('details/<int:pk>', views.pet_detail, name='pet_detail'),
    path('like/<int:pk>', views.pet_like, name='pet_like'),
    path('edit/<int:pk>', views.pet_edit, name='pet_edit'),
    path('delete/<int:pk>', views.pet_delete, name='pet_delete'),
]
