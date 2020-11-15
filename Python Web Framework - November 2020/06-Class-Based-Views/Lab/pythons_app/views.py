from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView
from .mixins import GroupRequiredMixin
from .models import Python
from .forms import PythonCreateModelForm


class Index(ListView):
    model = Python
    context_object_name = 'pythons'
    template_name = 'index.html'


class CreatePython(GroupRequiredMixin, FormView):
    template_name = 'create.html'
    form_class = PythonCreateModelForm
    group_required = ['User']

    def form_valid(self, form):
        form.save()
        return redirect('index')
