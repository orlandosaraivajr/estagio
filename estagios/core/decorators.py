from django.shortcuts import redirect

from estagios import settings


def area_student(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = settings.HOME_URL

    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_student:
                return function(request, *args, **kwargs)
            else:
                return redirect(redirect_url)
        else:
            return redirect(redirect_url)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
