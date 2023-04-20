from django import forms
from django.contrib.auth.forms import AuthenticationForm

# Создание формы Регистрации
class Registration(forms.Form):
    username = forms.CharField(label="Username", required=False, max_length=10, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'id': 'floatingPassword', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", required=True, widget=forms.widgets.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'id': 'floatingPassword', 'placeholder': 'Password'}))
    email = forms.EmailField(label="Email", required=True, widget=forms.widgets.EmailInput(attrs={'type': 'email', 'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'name@example.com'}))


# Переназначение (На основе наследования) формы Входа
class Login(AuthenticationForm):
    username = forms.CharField(label="Имя", max_length=10, widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'id': "floatingInput", "placeholder": "Username"}))
    password = forms.CharField(label="Пароль", widget=forms.widgets.PasswordInput(attrs={'class': 'form-control', 'id': "floatingInput", "placeholder": "Password"}))