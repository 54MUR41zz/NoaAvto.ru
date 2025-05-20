from django import forms
from .models import User

class TestForm(forms.Form):
    text_field = forms.CharField(
        label="Тестовое поле ввода",
        max_length=63,
        min_length=3,
        required=True
    )

    age_field = forms.IntegerField(
        label="Age",
        min_value=14,
        max_value=90,
        required=True
    )

    password_field = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        max_length=32,
        min_length=8,
        required=True
    )

class CarForm(forms.Form):
    mark = forms.CharField(
        max_length=2020,
        min_length=5,
        required=True
    )
    release_date = forms.CharField(
        max_length=2020,
        min_length=5,
        required=True
    )
    count_pages = forms.IntegerField(
        min_value=1,
    )

    author = forms.ModelChoiceField(queryset=User.objects.all())

class SignUpForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)