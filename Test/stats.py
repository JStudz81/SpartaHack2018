from .models import Stat, Character
from django.db.models import Sum
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
'''
Calculates total kills per user or character
'''
def total_kills(char_or_user):
    char = ''
    try:
        char = Character.objects.get(name=char_or_user)
    except ObjectDoesNotExist:
        pass
    if char:
        n = Stat.objects.filter(char_inst__char_id=char.id).all()
        kills = n.aggregate(Sum('kills'))
        kills = kills['kills__sum']
        return kills

    user = User.objects.get(username=char_or_user)

    if user:
        n = Stat.objects.filter(char_inst__user_id=user.id).all()
        kills = n.aggregate(Sum('kills'))
        kills = kills['kills__sum']
        return kills
'''
Calculates total amount of wins per user of character
'''
def num_wins(char_or_user):
    char = ''
    try:
        char = Character.objects.get(name=char_or_user)
    except ObjectDoesNotExist:
        pass
    if char:
        n = Stat.objects.filter(char_inst__char_id=char.id).all()
        num_wins = n.aggregate(Sum('wins'))
        num_wins = num_wins['wins__sum']
        return num_wins

    user = User.objects.get(username=char_or_user)
    if user:
        n = Stat.objects.filter(char_inst__user_id=user.id).all()
        num_wins = n.aggregate(Sum('wins'))
        num_wins = num_wins['wins__sum']
        return num_wins

'''
Calculates the win loss ratio per user or character
'''
def wl_ratio(char_or_user):
    char = ''
    try:
        char = Character.objects.get(name=char_or_user)
    except ObjectDoesNotExist:
        pass
    if char:
        n = Stat.objects.filter(char_inst__char_id=char.id).all()
        num_wins = n.aggregate(Sum('wins'))
        num_wins = num_wins['wins__sum']
        num_losses = n.count() - num_wins
        return (num_wins/num_losses)

    user = User.objects.get(username=char_or_user)
    if user:
        n = Stat.objects.filter(char_inst__user_id=user.id).all()
        num_wins = n.aggregate(Sum('wins'))
        num_wins = num_wins['wins__sum']
        num_losses = n.count() - num_wins
        return (num_wins/num_losses)
"""
def most_kills(char_or_user):
    ""
    Parameters: Enter either a char or user query set
    Returns the collection of objects that have the highest number of kills
    ""

    def id_from_name:
        if Stat.objects.filter(name=str(char_or_user)):
            n = Stat.objects.filter(name=str(char_or_user)).get().id
            Character.objects.all(pk=n)

            for k in


    #for character in sp_col:
    #    max_kills = 0
    #    max_kills += 1
    #max_kills = sp_col.aggregate(Max('kills'))
    #max_kills_col = specific_col.all(kills = max_kills)

    return max_kills_col


def num_wins(char_or_user):
    sp_col = Stat.objects.select_related(char_or_user)
    num_wins = sp_col.aggregate(Count(wins=True))
    return num_wins
"""