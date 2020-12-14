from django.contrib.auth.models import User
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic import CreateView, FormView
from django.views.generic.base import TemplateResponseMixin
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
            # TODO: ADD SIGNAL FOR USERPROFILE CREATION


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


class ProfileView(TemplateResponseMixin, View):
    template_name = 'user_profile.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user: User = None
        self.user_profile: UserProfile = None
        self.pets: Pet = None
        self.form: UserProfileModelForm = None

    def dispatch(self, request, *args, **kwargs):
        if self.request.method not in ('GET', 'POST'):
            raise HttpResponseBadRequest

        try:
            self.user = User.objects.get(pk=kwargs['pk'])
            self.user_profile = UserProfile.objects.get(user=self.user)
            self.pets = Pet.objects.filter(user=self.user_profile)
            self.form = UserProfileModelForm(instance=self.user)
        except (User.DoesNotExist, User.DoesNotExist, Pet.DoesNotExist):
            raise Http404

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        photo_name = self.user_profile.profile_picture.name.split('/')[-1]
        if photo_name != 'default.png':
            delete_image(self.user_profile.profile_picture.path)

        new_picture = self.request.FILES['profile_picture']
        self.user_profile.profile_picture = new_picture
        self.user_profile.save()
        return self.get(self.request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = {
            'user': self.user,
            'form': self.form,
            'profile_picture': self.user_profile.profile_picture,
            'pets': self.pets
        }
        context.update(**kwargs)
        return context
