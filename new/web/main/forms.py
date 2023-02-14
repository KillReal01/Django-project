from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput
from django import forms


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин'
    }))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Пароль'
    }))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Повтор пароля'
    }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            'password1': TextInput(attrs={
                'class': 'form-control',
                'type': 'password',
                'placeholder': 'Пароль'
            }),
            'password2': TextInput(attrs={
                'class': 'form-control',
                'type': 'password',
                'placeholder': 'Пароль'
            }),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин'
    }))
    password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Пароль'
    }))

