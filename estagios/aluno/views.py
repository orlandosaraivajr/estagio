from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render

from estagios.aluno.forms import CadastroForm
from estagios.aluno.models import CadastroModel
from estagios.core.decorators import area_student
from estagios.core.form import LoginForm
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
    form = LoginForm(request.POST)
    if not form.is_valid():
        return render(request, 'aluno_login.html')
    else:
        email = request.POST['username']
        password = request.POST['password']
        if registro_novo_aluno(email, password):
            auth_request(request)
            return redirect('aluno:aluno_home')
        else:
            return render(request, 'aluno_login.html')


@area_student
def home(request):
    context = {}
    return render(request, 'aluno_index.html', context)


@area_student
def sobre_mim(request):
    if request.method == "GET":
        dados = CadastroModel.objects.get(
            user=request.user
        ).__dict__
        context = {'form': CadastroForm(dados)}
    else:
        form = CadastroForm(request.POST)
        if not form.is_valid():
            context = {'form': form}
        else:
            CadastroModel.objects.update(**form.cleaned_data)
            dados = CadastroModel.objects.get(
                user=request.user
                ).__dict__
            context = {'form': CadastroForm(dados)}
    return render(request, 'aluno_sobre_mim.html', context)



@area_student
def cadastro_contato(request):
    context = {}
    return render(request, 'aluno_contato.html', context)


@area_student
def cadastro_faculdade(request):
    context = {}
    return render(request, 'aluno_faculdade.html', context)


@area_student
def cadastro_extensao(request):
    context = {}
    return render(request, 'aluno_outros_cursos.html', context)


@area_student
def cadastro_empregos_anteriores(request):
    context = {}
    return render(request, 'aluno_outros_empregos.html', context)


@area_student
def diario_aprendizado(request):
    context = {}
    return render(request, 'aluno_diario_aprendizado.html', context)


@area_student
def esqueceu_senha(request):
    context = {}
    return render(request, 'aluno_contato.html', context)
