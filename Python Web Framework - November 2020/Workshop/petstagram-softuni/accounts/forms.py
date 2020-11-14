from django import forms
from accounts.models import UserProfile


class UserProfileModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
