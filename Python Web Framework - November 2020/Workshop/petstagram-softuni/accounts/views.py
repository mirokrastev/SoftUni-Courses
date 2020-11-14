from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import UserProfileModelForm, LoginForm
from accounts.models import UserProfile
from pets.common import delete_image
from pets.models import Pet


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username, password = form.cleaned_data['username'], form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)

            UserProfile.objects.create(user=user,
                                       profile_picture='images/default.png')
            login(request, user)
            return redirect('landing')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username, password = form.cleaned_data['username'], form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('landing')
        error = 'Incorrect username or password'
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form, 'error': error})


@login_required
def logout_view(request):
    if request.method != 'POST':
        return Http404

    logout(request)
    return redirect('landing')


@login_required
def profile(request, pk):
    user = User.objects.get(pk=pk)
    profile_picture = UserProfile.objects.get(user=user)
    pets = Pet.objects.filter(user=profile_picture)

    if request.method == 'POST':
        photo_name = profile_picture.profile_picture.name.split('/')[-1]
        if photo_name != 'default.png':
            delete_image(profile_picture.profile_picture.path)

        new_picture = request.FILES['profile_picture']
        profile_picture.profile_picture = new_picture
        profile_picture.save()

    form = UserProfileModelForm(instance=user)

    context = {
        'user': user,
        'form': form,
        'profile_picture': profile_picture.profile_picture,
        'pets': pets
    }

    return render(request, 'user_profile.html', context)
