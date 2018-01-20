from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
import logging
from django.contrib.auth import logout


from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', {})
    else:
        return HttpResponseRedirect('login/')


def user_info(request, user_id):
    return

def showLogin(request):
    logger = logging.getLogger(__name__)

    logger.info('logging')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            logger.info('Made it')
            # Redirect to a success page.
            return HttpResponseRedirect('/')

        else:
            # Return an 'invalid login' error message.
            ...
            logger.info('no Made it')
            return render(request, 'login.html', {})

    else:
        return render(request, 'login.html', {})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')
