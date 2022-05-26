from django import forms

class CarForm(forms.Form):
    name = forms.CharField(max_length=50)
    mark = forms.CharField(max_length=50)
    price = forms.FloatField()
    year = forms.IntegerField()

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class SearchForm(forms.Form):
    search = forms.CharField(max_length=10)

