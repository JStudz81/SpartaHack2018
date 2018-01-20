from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
import logging
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Character, CharInst
from .models import GameTitle



from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        games = GameTitle.objects.filter(character__characters__user=request.user).distinct()



        return render(request, 'index.html', {'games': games})
    else:
        return HttpResponseRedirect('login/')

def user_info(request, user_id):
    # Test.models.objects.get(request)
    print("Found request")
    return

def showLogin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirect to a success page.
            return HttpResponseRedirect('/')

        else:
            # Return an 'invalid login' error message.
            ...

            return render(request, 'login.html', {})

    else:
        return render(request, 'login.html', {})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)

        return HttpResponseRedirect('/login/')

    else:
        return render(request, 'register.html', {})

