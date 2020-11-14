from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('profile/<int:pk>', views.profile, name='profile'),
]
