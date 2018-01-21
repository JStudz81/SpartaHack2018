from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
import logging
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Character, CharInst
from .models import GameTitle, Stat
from django.db.models import Sum
from . import stats



from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        games = GameTitle.objects.filter(characters__char_insts__user_id=request.user.id).distinct()


        return render(request, 'index.html', {'games': games})
    else:
        return HttpResponseRedirect('login/')

def user_info(request, user_id):
    games = GameTitle.objects.filter(characters__char_insts__user_id=request.user.id).distinct()
    user = User.objects.get(pk=user_id)
    user_games = GameTitle.objects.filter(characters__char_insts__user_id=user_id).all().distinct()
    user_stats = Stat.objects.filter(char_inst__user_id=user_id).all()
    numGames = user_stats.count()

    chars_played_most = stats.rank(user.id)

    context = {
        'user': user,
        'user_games': user_games,
        'user_stats': user_stats,
        'games': games,
        'wins': stats.num_wins(user.username),
        'wlRatio': stats.wl_ratio(user.username),
        'numGames': numGames,
        'losses': numGames - stats.num_wins(user.username),
        'chars_played': chars_played_most[:10]
    }

    return render(request, 'user.html', context)

def character_info(request, character_id):
    games = GameTitle.objects.filter(characters__char_insts__user_id=request.user.id).distinct()
    character = Character.objects.get(pk=character_id)
    character_game = GameTitle.objects.filter(characters__name__exact=character.name).get()
    character_stats = Stat.objects.filter(char_inst__char_id=character_id).all()
    numGames = character_stats.count()


    context = {
        'char': character,
        'character_game': character_game,
        'character_stats': character_stats,
        'games': games,
        'wins': stats.num_wins(character.name),
        'wlRatio': stats.wl_ratio(character.name),
        'numGames': numGames,
        'losses': numGames - stats.num_wins(character.name),

    }

    return render(request, 'character.html', context)


def addGame(request):
    if request.method == 'POST':
        game, created = GameTitle.objects.get_or_create(game_title=request.POST['game'])
        if created:
            game.save()

        char, created = Character.objects.get_or_create(name=request.POST['char'], game_id=game.id)
        if created:
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
    chars = CharInst.objects.filter(char__game_id=game.id)

    stats = Stat.objects.filter(char_inst__char__game=game)

    games_played = stats.count()
    wins = stats.filter(wins=True).count()

    losses = games_played - wins

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
    games = GameTitle.objects.filter(characters__char_insts__user=request.user).distinct()
    char_inst = CharInst.objects.get(pk=character_id)
    char = Character.objects.filter(char_insts=char_inst).get().name
    stats = Stat.objects.filter(char_inst_id=character_id)

    games_played = stats.count()
    wins = stats.filter(wins=True).count()

    losses = games_played - wins


    kills = stats.aggregate(Sum('kills'))
    deaths = stats.aggregate(Sum('deaths'))
    damageDealt = stats.aggregate(Sum('damage_dealt'))
    damageReceived = stats.aggregate(Sum('damage_received'))

    context = {
        'games': games,
        'character_id': character_id,
        'char_name': char,
        'games_played': games_played,
        'wins': wins,
        'losses': losses,
        'kills': kills,
        'deaths': deaths,
        'damageDealt': damageDealt,
        'damageReceived': damageReceived
    }

    return render(request, 'character_page.html', context)


def addStat(request, character_id):

    if request.method == 'POST':

        char = CharInst.objects.get(pk=character_id)

        win = request.POST['win']
        kills = request.POST['kills']
        deaths = request.POST['deaths']
        dam_given = request.POST['given']
        dam_taken = request.POST['received']

        q = Stat(wins=win, kills=kills, deaths=deaths, damage_dealt=dam_given, damage_received=dam_taken)
        q.char_inst = char
        q.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def addCharacter(request, game_id):
    if request.method == 'POST':

        game = GameTitle.objects.get(pk=game_id)

        name = request.POST['name']

        char = Character.objects.create(name=name, game=game)
        char.save()

        charInst = CharInst.objects.create(user=request.user, char=char)
        charInst.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def search(request):
    if request.method == 'POST':
        param = request.POST['search']
        try:
            user = User.objects.get(username=param)
            return HttpResponseRedirect('/user/' + str(user.id))
        except:
            try:
                character = Character.objects.get(name=param)
                return HttpResponseRedirect('/character_info/' + str(character.id))
            except:
                return HttpResponseRedirect('/')
def battles():
    return

def allGames(request):
    games = GameTitle.objects.filter(characters__char_insts__user=request.user).distinct()
    allGames = GameTitle.objects.all()

    context = {
        'allGames': allGames,
        'games': games
    }

    return render(request, "allGames.html", context)
