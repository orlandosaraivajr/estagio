from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render

from estagios.core.decorators import area_student
from estagios.core.functions import auth_request
from estagios.core.functions import registro_novo_aluno


def login(request):
    if request.method == "GET":
        return render(request, 'aluno_login.html')
    else:
        if auth_request(request):
            return redirect('aluno:aluno_home')
        else:
            return render(request, 'aluno_login.html')


def logout(request):
    auth_logout(request)
    return render(request, 'aluno_login.html')


def cadastro_inicial(request):
    if request.method == "GET":
        return render(request, 'aluno_cadastro_inicial.html')
    else:
        return efetivar_cadastro_aluno(request)


def efetivar_cadastro_aluno(request):
    registro_novo_aluno(request)
    if auth_request(request):
        return redirect('aluno:aluno_home')
    else:
        return render(request, 'aluno_login.html')


@area_student
def cadastro_dados_pessoais(request):
    context = {}
    return render(request, 'aluno_cadastro.html', context)


@area_student
def home(request):
    context = {}
    return render(request, 'aluno_index.html', context)


@area_student
def esqueceu_senha(request):
    context = {}
    return render(request, 'aluno_cadastro.html', context)
