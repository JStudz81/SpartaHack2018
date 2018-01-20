from django.contrib.auth.models import User
from . import models

'''Enter either a char or user query set
Returns the collection of objects that have the highest number of kills
'''
def most_kills(char_or_user):
    max_kills = 0
    specific_col = models.Stat.objects.select_related(char_or_user)
    for character in specific_col:
        max_kills = 0
        max_kills
    max_kills = specific_col.aggregate(Max('kills'))
    max_kills_col = specific_col.all(kills = max_kills)
    '''
    user = max_kills_col.User
    char = max_kills_col.Character
    time = max_kills_col.time_stamp
    '''
    return max_kills_col

def num_wins(char_or_user):
    specific_col = models.Stat.objects.select_related(char_or_user)
    num_wins = specific_col.aggregate(Count(wins=True))
    return num_wins