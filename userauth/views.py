from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render


def login(request):
    """

    :param request:
    :return:
    """
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/design/")
        else:
            return render(request, 'userauth/login.html', {'invalid': True})
    elif request.user.is_authenticated():

        return HttpResponseRedirect('/design')

    return render(request, 'userauth/login.html')


def logout(request):
    """

    :param request:
    :return:
    """
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    auth.logout(request)
    return render(request, 'userauth/login.html', {'logged_out': True})

