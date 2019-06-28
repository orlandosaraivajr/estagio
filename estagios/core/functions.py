from datetime import datetime

import pytz
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login

from estagios.aluno.models import SobreMimModel, ContatoModel, RedesSociaisModel


def authenticate(username=None, password=None):
    User = get_user_model()
    try:
        user = User.objects.get(email=username)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user
    return None


def auth_request(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
    except:
        return False
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return True
    else:
        return False


def registro_novo_aluno(email=None, password=None):
    if email and password:
        User = get_user_model()
        novo_aluno = User.objects.create_user(
            email, email, password, is_student=True)
        novo_aluno.save()
        cadastro = SobreMimModel()
        cadastro.user = novo_aluno
        cadastro.data_nascimento = datetime(2000, 1, 1, 0, 0, 0, tzinfo=pytz.UTC)
        cadastro.save()
        cadastro = ContatoModel()
        cadastro.user = novo_aluno
        cadastro.save()
        cadastro = RedesSociaisModel()
        cadastro.user = novo_aluno
        cadastro.save()
        return True
    else:
        return False
