from .models import Stat, Character
from django.db.models import Sum
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist



def temp_search(character):
    char = ''
    try:
        char = Character.objects.get(name=character)
        return True
    except ObjectDoesNotExist:
        pass


'''
Calculates total kills per user or character
'''
def total_kills(char_or_user):

    if temp_search(char_or_user) == True:
        char = Character.objects.get(name=char_or_user)
        n = Stat.objects.filter(char_inst__char_id=char.id).all()
        kills = n.aggregate(Sum('kills'))
        kills = kills['kills__sum']
        return kills

    else:
        user = User.objects.get(username=char_or_user)
        n = Stat.objects.filter(char_inst__user_id=user.id).all()
        kills = n.aggregate(Sum('kills'))
        kills = kills['kills__sum']
        return kills

def total_kills_b(char, user):
    char = Character.objects.get(name=char)
    user = User.objects.get(username=user)
    m = Stat.objects.filter(char_inst__char=char).filter(char_inst__user=user).all()
    kills = m.aggregate(Sum('kills'))
    kills = kills['kills__sum']
    return kills

'''
Calculates the K/D Ratio of a certain character for a user
'''
def kd_ratio(char, user):
    char = Character.objects.get(name=char)
    user = User.objects.get(username=user)
    m = Stat.objects.filter(char_inst__char=char).filter(char_inst__user=user).all()
    kills = m.aggregate(Sum('kills'))
    deaths = m.aggregate(Sum('deaths'))
    kills = kills['kills__sum']
    deaths = deaths['deaths__sum']
    return round(kills/deaths, 3)

'''
Calculates total amount of wins per user of character
'''
def num_wins(char_or_user):

    if temp_search(char_or_user) == True:
        char = Character.objects.get(name=char_or_user)
        n = Stat.objects.filter(char_inst__char_id=char.id).all()
        num_wins = n.aggregate(Sum('wins'))
        num_wins = num_wins['wins__sum']
        return num_wins

    else:
        user = User.objects.get(username=char_or_user)
        n = Stat.objects.filter(char_inst__user_id=user.id).all()
        num_wins = n.aggregate(Sum('wins'))
        num_wins = num_wins['wins__sum']
        return num_wins

'''
Calculates the win loss ratio per user or character
'''
def wl_ratio(char_or_user):

    if temp_search(char_or_user):
        char = Character.objects.get(name=char_or_user)
        n = Stat.objects.filter(char_inst__char_id=char.id).all()
        num_wins = n.aggregate(Sum('wins'))
        num_wins = num_wins['wins__sum']
        num_losses = n.count() - num_wins
        return (num_wins/num_losses)


    else:
        user = User.objects.get(username=char_or_user)
        n = Stat.objects.filter(char_inst__user_id=user.id).all()
        num_wins = n.aggregate(Sum('wins'))
        num_wins = num_wins['wins__sum']
        num_losses = n.count() - num_wins
        return (num_wins/num_losses)
