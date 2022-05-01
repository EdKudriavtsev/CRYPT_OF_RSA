from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from main.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    agreement_checked = forms.BooleanField(
        label='Я принимаю условия соглашения',
        widget=forms.CheckboxInput()
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class EditVotingForm(forms.Form):
    title = forms.CharField(
        label='Название голосования',
        required=True
    )
    description = forms.CharField(
        label='Описание голосования',
        required=True
    )


class EditProfileForm(forms.Form):
    username = forms.CharField(
        label='Имя пользователя',
        required=True
    )
    email = forms.CharField(
        label='Email',
        required=True
    )


class CipherForm(forms.Form):
    text = forms.CharField(
        label='Исходный текст',
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Введите текст для шифрования...'})
    )
    key = forms.IntegerField(
        label='ключ',
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'ключ'})
    )
    key2 = forms.IntegerField(
        label='число n',
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'число n'})
    )
    encrypt_decrypt = forms.ChoiceField(label='', choices=(
        ("1", "Зашифровать"),
        ("2", "Расшифровать"),
    ))
