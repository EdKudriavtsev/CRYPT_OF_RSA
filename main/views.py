import datetime
from sqlite3 import IntegrityError

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from main.models import User, CipherHistory
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse

from main.forms import EditProfileForm, RegistrationForm, CipherForm

from main.algorithms.cipher import Cipher


def get_menu_context():
    return [
        {},
    ]


def get_base_context(pagename):
    context = {
        'pagename': pagename,
        'menu': get_menu_context()
    }
    return context


def index_page(request):
    if request.user.is_authenticated:
        return redirect('cipher')
    context = get_base_context('Главная')
    return render(request, 'pages/index.html', context)


@login_required
def profile_page(request):
    context = {
        'menu': get_menu_context(),
        'pagename': 'Профиль',
    }
    return render(request, 'pages/profile/profile.html', context)


@login_required
def profile_edit_page(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {
        'menu': get_menu_context(),
        'pagename': ' Редактирование профиля',
        'form': EditProfileForm(),
        'user': get_object_or_404(User, id=user_id),
    }
    if request.method == "POST":
        form = EditProfileForm(request.POST)

        if form.is_valid():
            try:
                user.username = form.cleaned_data['username']
                user.email = form.cleaned_data['email']
                user.save()
                messages.success(request, 'Изменения сохранены', 'alert-success')
            except IntegrityError:
                messages.error(request, 'Данное имя уже существует', 'alert-error')

        return redirect('profile')
    return render(request, 'pages/profile/profile_edit.html', context)


def registration_page(request):
    if request.user.is_authenticated:
        messages.error(request, "Залогиненный пользователь не может регистрироваться",
                       extra_tags='alert-danger')
    context = get_base_context('Регистрация')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_pass = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_pass)
            login(request, user)
            return redirect(reverse('index'))
    else:
        form = RegistrationForm()
    context['form'] = form
    return render(request, 'registration/registration.html', context)


def cipher_page(request):
    context = get_base_context('Шифратор')
    if request.method == 'POST':
        form = CipherForm(request.POST)
        if form.is_valid():
            str_in = form.data['text']
            key = form.data['key']
            key2 = form.data['key2']
            condition = form.data['encrypt_decrypt']

            if condition == "1":
                result = Cipher.encrypt(str_in, int(key), int(key2))
            elif condition == "2":
                result = Cipher.decrypt(str_in, int(key), int(key2))
            else:
                result = Cipher.decrypt(str_in, int(key), int(key2))

            if request.user.is_authenticated:
                item = CipherHistory(date=datetime.datetime.now(), str_in=str_in, key=key, key2=key2, result=result,
                                     author=request.user)
                item.save()

            context['result'] = result
            context['form'] = form
        else:
            context['form'] = form
    else:
        context['form'] = CipherForm()

    return render(request, 'pages/cipher.html', context)
