from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic import CreateView, FormView
from accounts.forms import UserProfileModelForm, LoginForm
from accounts.models import UserProfile
from pets.common import delete_image
from pets.models import Pet


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    context_object_name = 'form'

    def form_valid(self, form):
        if form.is_valid():
            form = form.save()
            UserProfile.objects.create(user=form, profile_picture='images/default.png')
            login(self.request, form)
            return redirect('landing')


class Login(FormView):
    form_class = LoginForm
    template_name = 'registration/login.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def form_valid(self, form):
        username, password = form.cleaned_data['username'], form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)

        if user:
            login(self.request, user)
            return redirect('landing')

        context = self.get_context_data()
        context['error'] = 'Incorrect username or password'
        return render(self.request, self.template_name, context)


class LogOut(View):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.method == 'POST':
            raise Http404
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        logout(self.request)
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
