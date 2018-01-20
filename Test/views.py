from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
import logging
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Character, CharInst
from .models import GameTitle, Stat
from django.db.models import Sum



from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        games = GameTitle.objects.filter(characters__char_insts__user_id=request.user.id).distinct()


        return render(request, 'index.html', {'games': games})
    else:
        return HttpResponseRedirect('login/')

def user_info(request, user_id):
    user = User.objects.get(pk=1)
    user.username
    print("request received")
    pass

def addGame(request):
    if request.method == 'POST':
        game = GameTitle.objects.create()
        game.game_title = request.POST['game']
        game.save()

        char = Character(name=request.POST['char'], game_id=game.id)
        char.save()

        char_inst = CharInst(char_id=char.id, user_id=request.user.id)
        char_inst.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

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

def game_view(request, game_id):
    game = GameTitle.objects.get(pk=game_id)
    games = GameTitle.objects.filter(characters__char_insts__user=request.user).distinct()
    chars = game.characters.all()

    stats = Stat.objects.filter(char_inst__char__game=game)

    games_played = stats.count()
    wins = stats.aggregate(Sum('wins'))
    if wins['wins__sum']:
        losses = games_played - wins['wins__sum']
    else:
        losses = None

    kills = stats.aggregate(Sum('kills'))
    deaths = stats.aggregate(Sum('deaths'))
    damageDealt = stats.aggregate(Sum('damage_dealt'))
    damageReceived = stats.aggregate(Sum('damage_received'))


    context = {
        'game': game,
        'games': games,
        'chars': chars,
        'games_played': games_played,
        'wins': wins,
        'losses': losses,
        'kills': kills,
        'deaths': deaths,
        'damageDealt': damageDealt,
        'damageReceived': damageReceived
    }
    return render(request, 'game_page.html', context)


def character_view(request, character_id):
    return HttpResponseRedirect('/')


def stat_form(request):

    if request.method == 'POST':

        wins = request.POST['Win']
        kills = request.POST['kills']
        deaths = request.POST['deaths']
        dam_given = request.POST['damage given']
        dam_taken = request.POST['damage taken']

        q = Stat(wins=wins, kills=kills, deaths=deaths, damage_dealt=dam_given, damage_received=dam_taken)
        q.user = username
        q.char = character
        q.save()

        return render(request, 'game_page.html', {'game': game})

"""
        form = CharUpdateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            char.health = form.cleaned_data['health']

            char.save()

            return HttpResponseRedirect('/' + character_id)

"""