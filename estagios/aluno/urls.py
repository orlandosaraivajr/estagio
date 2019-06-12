from django.urls import path

from . import views

app_name = 'aluno'

urlpatterns = [
    path('', views.home, name='aluno_home'),
    path('cadastro_inicial/', views.cadastro_inicial, name='aluno_cadastro_inicial'),
    path('login/', views.login, name='aluno_login'),
    path('logout/', views.logout, name='aluno_logout'),
    path('esqueci_senha/', views.esqueceu_senha, name='aluno_esqueceu_senha'),

    path('cadastro/', views.cadastro_dados_pessoais, name='aluno_cadastro_dados_pessoais'),
]
