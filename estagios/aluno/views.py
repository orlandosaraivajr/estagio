from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'aluno_index.html', context)

def cadastro_dados_pessoais(request):
    context = {}
    return render(request, 'aluno_cadastro.html', context)