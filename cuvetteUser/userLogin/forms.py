from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

# Create User
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Authenticate User
class LoginForm(forms.Form):
    username_or_email = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=PasswordInput())
