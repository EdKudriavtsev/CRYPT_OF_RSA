from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.http import urlencode


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
    if request.user.is_authenticated:
        context['avatar'] = request.user.get_avatar()
    return context


def index_page(request):
    if request.user.is_authenticated:
        return redirect('catalog')
    context = get_base_context('Главная', request)
    return render(request, 'pages/index.html', context)


@login_required
def profile_page(request):
    context = {
        'menu': get_menu_context(),
        'pagename': 'Профиль',
        'avatar': request.user.get_avatar(),
    }
    return render(request, 'pages/profile/profile.html', context)


@login_required
def profile_edit_page(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {
        'menu': get_menu_context(),
        'pagename': ' Редактирование профиля',
        'votings_count': ComparingReview.objects.filter(author=request.user).count(),
        'ratefact_count': ProductRateFact.objects.filter(user=request.user).count(),
        'form': EditProfileForm(),
        'user': get_object_or_404(User, id=user_id),
        'avatar': request.user.get_avatar()
    }
    context['form2'] = UploadUserAvatarForm(initial={
        'user': context['user']
    })
    if request.method == "POST":
        form = EditProfileForm(request.POST)
        form2 = UploadUserAvatarForm(request.POST, request.FILES)

        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()
            messages.success(request, 'Изменения сохранены', 'alert-success')

        if form2.is_valid():
            try:
                avatar = UserAvatar.objects.filter(user=request.user)[0]
                avatar.user = form2.cleaned_data['user']
                avatar.image = form2.cleaned_data['image']
                avatar.save()
            except IndexError:
                form2.save()
            messages.success(request, 'Аватар сохранен', 'alert-success')
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
            avatar = UserAvatar(
                user=user,
                image="https://html5book.ru/wp-content/uploads/2016/10/profile-image.png")
            avatar.save()
            user = authenticate(username=user.username, password=raw_pass)
            login(request, user)
            return redirect(reverse('index'))
    else:
        form = RegistrationForm()
    context['form'] = form
    return render(request, 'registration/registration.html', context)