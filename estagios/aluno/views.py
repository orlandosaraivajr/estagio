from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'aluno_index.html', context)
