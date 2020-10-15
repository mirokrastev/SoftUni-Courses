from django.shortcuts import render, redirect
from django.views import View
from .forms import BookModelForm, BookModel


def home(request):
    books = BookModel.objects.all()
    return render(request, 'index.html', {'books': books})


class CreateBook(View):
    def get(self, request):
        form = BookModelForm()
        return render(self.request, 'books/create_book.html', {'form': form})

    def post(self, request):
        form = BookModelForm(self.request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(self.request, 'books/create_book.html', {'form': form})


class EditBook(View):
    def get(self, request, book_pk):
        inst = BookModel.objects.get(pk=book_pk)
        form = BookModelForm(instance=inst)
        return render(request, 'books/edit_book.html', {'form': form})

    def post(self, request, book_pk):
        inst = BookModel.objects.get(pk=book_pk)
        form = BookModelForm(self.request.POST, instance=inst)
        if form.is_valid():
            form.save()
        return redirect('home')
