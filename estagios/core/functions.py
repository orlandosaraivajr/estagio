from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

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
