from django import forms
from expense_tracker.models import Expense, Profile


class ExpenseModelForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image_url', 'price')

        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
        }


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name')
