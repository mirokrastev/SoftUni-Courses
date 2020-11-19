from django.contrib.auth.decorators import login_required
from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='register_view'),
    path('login/', views.Login.as_view(), name='login_view'),
    path('logout/', login_required(views.LogOut.as_view()), name='logout_view'),
    path('profile/<int:pk>', views.profile, name='profile'),
]
