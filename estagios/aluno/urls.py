from django.urls import path
from . import views

app_name = 'aluno'

urlpatterns = [
    path('', views.home, name='aluno_home'),
    path('cadastro/', views.cadastro_dados_pessoais, name='aluno_cadastro_dados_pessoais'),
]