"""softuni_exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipes import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='home'),

    path('create', views.create_recipe, name='create_recipe'),

    path('edit/<int:id>', views.edit_recipe, name='edit_recipe'),
    path('delete/<int:id>', views.delete_recipe, name='delete_recipe'),
    path('details/<int:id>', views.detail_recipe, name='detail_recipe'),
]
