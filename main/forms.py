from django import forms
from django.contrib.auth.forms import UserCreationForm

from main.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    agreement_checked = forms.BooleanField(
        label='Я принимаю условия соглашения',
        widget=forms.CheckboxInput()
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


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
        widget=forms.NumberInput(attrs={'placeholder': 'ключ'}),
        max_value=5000000,
        min_value=0
    )
    key2 = forms.IntegerField(
        label='число n',
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'число n'}),
        max_value=5000000,
        min_value=0
    )
    encrypt_decrypt = forms.ChoiceField(label='', choices=(
        ("1", "Зашифровать"),
        ("2", "Расшифровать"),
    ))
