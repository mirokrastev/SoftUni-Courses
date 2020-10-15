from django import forms
from labche.models import BookModel


class BookModelForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ('title', 'pages', 'author', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }
