from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
            context = {}
            return render(request, 'aluno_index.html', context)
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

