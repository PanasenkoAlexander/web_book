from django import forms

# Создание формы Регистрации
class Registration(forms.Form):
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!
    username = forms.CharField(label="Password", required=True, widget=forms.widgets.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'id': 'floatingPassword', 'placeholder': 'Password'}))
    password = forms.CharField(label="Password", required=True, widget=forms.widgets.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'id': 'floatingPassword', 'placeholder': 'Password'}))
    email = forms.EmailField(label="Email", required=True, widget=forms.widgets.EmailInput(attrs={'type': 'email', 'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'name@example.com'}))
