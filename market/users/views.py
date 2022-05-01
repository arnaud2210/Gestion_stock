from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import logout, get_user_model, login, authenticate

User = get_user_model()


def login_page(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        # fonction pour créer un utilisateur et le connecter directement
        # User.objects.create_user(username=username, password=password)

        # fonction pour connecter un utilisateur
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('categories')

    return render(
        request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
