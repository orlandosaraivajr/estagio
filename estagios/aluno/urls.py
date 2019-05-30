from django.urls import path
from . import views

app_name = 'aluno'

urlpatterns = [
    path('', views.home,name='aluno_home'),
]