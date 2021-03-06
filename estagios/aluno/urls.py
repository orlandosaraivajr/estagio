from django.urls import path

from . import views

app_name = 'aluno'

urlpatterns = [
    path('login/', views.login, name='aluno_login'),
    path('logout/', views.logout, name='aluno_logout'),
    path('cadastro_inicial/', views._cadastro_inicial, name='aluno_cadastro_inicial'),
    path('esqueci_senha/', views.esqueceu_senha, name='aluno_esqueceu_senha'),

    path('', views.home, name='aluno_home'),
    path('sobremim/', views.sobre_mim, name='aluno_sobre_mim'),
    path('contato/', views.contato, name='aluno_contato'),
    path('redessociais/', views.redes_sociais, name='aluno_redes_sociais'),

    path('faculdade/', views.faculdade, name='aluno_faculdade'),
    path('faculdade/cadastro/', views.faculdade_cadastro, name='aluno_faculdade_cadastro'),
    path('faculdade/editar/', views.faculdade_editar, name='aluno_faculdade_editar'),
    path('faculdade/excluir/', views.faculdade_excluir, name='aluno_faculdade_excluir'),

    path('outros_cursos/', views.cadastro_extensao, name='aluno_outros_cursos'),
    path('empregos_anteriores/', views.cadastro_empregos_anteriores, name='aluno_outros_empregos'),
    path('diario_aprendizado/', views.diario_aprendizado, name='aluno_diario_aprendizado'),

]
