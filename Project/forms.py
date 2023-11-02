from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length = 254, help_text='Обязательное поле')
    first_name = forms.CharField(required = True, label = "Ваше имя", max_length = 254)
    class Meta:
        model = User
        fields = ('first_name', 'email', 'username', 'password1', 'password2')