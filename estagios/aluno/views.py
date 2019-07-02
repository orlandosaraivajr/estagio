from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render

from estagios.aluno.forms import SobreMimForm, ContatoForm, RedesSociaisForm, FaculdadeForm
from estagios.aluno.models import SobreMimModel, ContatoModel, RedesSociaisModel, FaculdadeModel
from estagios.core.decorators import area_student
from estagios.core.form import LoginForm, NomeCompletoForm
from estagios.core.functions import auth_request
from estagios.core.functions import registro_novo_aluno
from estagios.core.models import User


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
        return _efetivar_cadastro(request)


def _efetivar_cadastro(request):
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


def _atualizar_dados_sobre_mim(request):
    form = SobreMimForm(request.POST)
    form_nome = NomeCompletoForm(request.POST)
    form_nome.is_valid()
    if not form.is_valid() and not form_nome.is_valid():
        context = {'form': form,
                   'formUsername': form_nome}
    else:
        SobreMimModel.objects.update(**form.cleaned_data)
        User.objects.update(**form_nome.cleaned_data)
        dados = SobreMimModel.objects.get(user=request.user).__dict__
        dados_user = User.objects.get(email=request.user).__dict__
        context = {'form': SobreMimForm(dados),
                   'formUsername': NomeCompletoForm(dados_user)}
    return context


def _atualizar_contato(request):
    form = ContatoForm(request.POST)
    if not form.is_valid():
        context = {'form': form}
    else:
        ContatoModel.objects.update(**form.cleaned_data)
        dados = ContatoModel.objects.get(user=request.user).__dict__
        context = {'form': ContatoForm(dados)}
    return context


def _atualizar_redes_sociais(request):
    form = RedesSociaisForm(request.POST)
    if not form.is_valid():
        context = {'form': form}
    else:
        RedesSociaisModel.objects.update(**form.cleaned_data)
        dados = RedesSociaisModel.objects.get(user=request.user).__dict__
        context = {'form': RedesSociaisForm(dados)}
    return context


def _cadastrar_faculdade(request):
    form = FaculdadeForm(request.POST)
    form.is_valid()
    if not form.is_valid():
        context = {
            'form': form,
            }
    else:
        faculdade = FaculdadeModel(**form.cleaned_data)
        faculdade.user = request.user
        faculdade.save()
        context = {'form': FaculdadeForm()}
    return context

@area_student
def home(request):
    context = {}
    return render(request, 'aluno_index.html', context)


@area_student
def sobre_mim(request):
    if request.method == "GET":
        dados = SobreMimModel.objects.get(user=request.user).__dict__
        dados_user = User.objects.get(email=request.user).__dict__
        context = {'form': SobreMimForm(dados),
                   'formUsername': NomeCompletoForm(dados_user)}
    else:
        context = _atualizar_dados_sobre_mim(request)
    return render(request, 'aluno_sobre_mim.html', context)


@area_student
def contato(request):
    if request.method == "GET":
        dados = ContatoModel.objects.get(user=request.user).__dict__
        context = {'form': ContatoForm(dados)}
    else:
        context = _atualizar_contato(request)
    return render(request, 'aluno_contato.html', context)


@area_student
def redes_sociais(request):
    if request.method == "GET":
        dados = RedesSociaisModel.objects.get(user=request.user).__dict__
        context = {'form': RedesSociaisForm(dados)}
    else:
        context = _atualizar_redes_sociais(request)
    return render(request, 'aluno_redes_sociais.html', context)


@area_student
def faculdade(request):
    context = {}
    return render(request, 'aluno_faculdade.html', context)


@area_student
def faculdade_cadastro(request):
    if request.method == "GET":
        context = {'form': FaculdadeForm()}
    else:
        context = _cadastrar_faculdade(request)
    return render(request, 'aluno_faculdade_cadastrar.html', context)

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
