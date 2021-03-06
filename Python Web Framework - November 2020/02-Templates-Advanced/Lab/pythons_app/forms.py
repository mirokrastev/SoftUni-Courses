from django import forms
from .models import Python


class PythonCreateModelForm(forms.ModelForm):
    class Meta:
        model = Python
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'image': forms.TextInput(attrs={'class': 'form-control'}),
        }
        fields = ('name', 'description', 'image')
