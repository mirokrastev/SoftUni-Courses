from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from .models import Python
from .forms import PythonCreateModelForm
from .decorators import allowed_groups


def index(request):
    pythons = Python.objects.all()
    return render(request, 'index.html', {'pythons': pythons})


@allowed_groups(['User'])
def create(request):
    if request.user.is_superuser:
        print(request.user.groups.all())
    if request.method == 'POST':
        form = PythonCreateModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = PythonCreateModelForm()
    context = {'form': form}
    return render(request, 'create.html', context)


def login_view(request):
    user = authenticate(request, username='test_user', password='qwerasd123')
    if user:
        login(request, user)
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')