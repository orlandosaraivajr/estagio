from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from estagios import settings


def area_student(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = settings.HOME_URL

    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_student:
                return function(request, *args, **kwargs)
            else:
                return redirect(redirect_url)
        else:
            return redirect(redirect_url)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


@area_student
@login_required
def home(request):
    context = {}
    return render(request, 'aluno_index.html', context)


def login(request):
    if request.method == "GET":
        return render(request, 'aluno_login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('aluno:aluno_home')
        else:
            context = {'acesso_negado': True}
            return render(request, 'aluno_login.html', context)


def logout(request):
    auth_logout(request)
    return render(request, 'aluno_login.html')


def cadastro_dados_pessoais(request):
    context = {}
    return render(request, 'aluno_cadastro.html', context)


def esqueceu_senha(request):
    context = {}
    return render(request, 'aluno_cadastro.html', context)
