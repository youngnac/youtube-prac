from django import forms
from django.contrib.auth.forms import UserCreationForm

from member.models import MyUser


class LoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(max_length=30)


class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email']
