from django.urls import path
from expense_tracker import views

urlpatterns = [
    path('', views.home, name='home'),

    path('create', views.create_expense, name='create'),
    path('edit/<int:pk>', views.edit_expense, name='edit'),
    path('delete/<int:pk>', views.delete_expense, name='delete'),

    path('profile', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile/delete', views.profile_delete, name='profile_delete'),
]
