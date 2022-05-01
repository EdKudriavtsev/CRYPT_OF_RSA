from sqlite3 import IntegrityError

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from main.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.http import urlencode

from main.forms import EditProfileForm, RegistrationForm


def get_menu_context():
    return [
        {'url_name': 'index', 'name': 'Главная'},
    ]


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def get_base_context(pagename, request):
    context = {
        'pagename': pagename,
        'menu': get_menu_context()
    }
    return context


def index_page(request):
    context = get_base_context('Главная', request)
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
    context = get_base_context('Регистрация', request)
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