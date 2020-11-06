from django.shortcuts import render, redirect
from .models import Python
from .forms import PythonCreateModelForm


def index(request):
    pythons = Python.objects.all()
    return render(request, 'index.html', {'pythons': pythons})


def create(request):
    if request.method == 'POST':
        form = PythonCreateModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = PythonCreateModelForm()
    context = {'form': form}
    return render(request, 'create.html', context)
