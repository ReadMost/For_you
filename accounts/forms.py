from django import forms

class SigninForm(forms.Form):
    email = forms.CharField(
    label = "",
    widget = forms.TextInput(attrs={
        'class':'email',
        'placeHolder':'Email'
    }))
    password = forms.CharField(
    label = "",
    widget = forms.PasswordInput(attrs={
        'class':'password',
        'placeholder':'Введите пароль'
    }))


class SignupForm(forms.Form):
    email = forms.CharField(
        label = "",
        widget = forms.TextInput(attrs={
        'class':'input',
        'placeHolder':'Email'
    }))
    username = forms.CharField(
        label = "",
        widget = forms.TextInput(attrs={
        'class':'input',
        'placeHolder':'Полное имя'
    }))
    password = forms.CharField(
        label = "",
        widget = forms.PasswordInput(attrs={
        'class':'input',
        'placeholder':'Пароль'
    }))
    password_repeat = forms.CharField(
        label = "",
        widget = forms.PasswordInput(attrs={
        'class':'input',
        'placeholder':'Введите пароль повторно'
    }))
    
    