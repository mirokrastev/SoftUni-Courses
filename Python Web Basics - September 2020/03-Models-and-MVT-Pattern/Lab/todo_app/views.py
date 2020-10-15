from django.shortcuts import render
from todo_app.models import Todo


def home(request):
    content = {'todos': Todo.objects.all()}
    return render(request, 'todo_app/index.html', content)
