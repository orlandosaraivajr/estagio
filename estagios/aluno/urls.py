from django.urls import path

from . import views

app_name = 'aluno'

urlpatterns = [
    path('login/', views.login, name='aluno_login'),
    path('logout/', views.logout, name='aluno_logout'),
    path('cadastro_inicial/', views.cadastro_inicial, name='aluno_cadastro_inicial'),
    path('esqueci_senha/', views.esqueceu_senha, name='aluno_esqueceu_senha'),

    path('', views.home, name='aluno_home'),
    path('sobremim/', views.sobre_mim, name='aluno_sobre_mim'),
    path('contato/', views.cadastro_contato, name='aluno_contato'),
]
