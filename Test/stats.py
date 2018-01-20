
from . import models
import db.sqlite3

from Test.models.py import Stat

def total_kills(char_or_user):

    if Stat.objects.filter(name=char_or_user):
        n = Stat.objects.filter(name=char_or_user).get().id
        group = Stat.objects.filter(char_inst.char_id = n)
        kills = group.objects.aggregate(Sum(Stat.kills))

    if Stat.objects.filter(username=str(char_or_user)):
        n = Stat.objects.filter(username=str(char_or_user)).get().id
        group = Stat.objects.filter(char_inst.char_id = n)
        kills = group.objects.aggregate(Sum(Stat.kills))\

    return kills

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
