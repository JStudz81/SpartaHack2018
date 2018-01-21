
### WELCOME TO BATTLES ###

"""
Battles is a battleground where worthy opponents can come to find the most even match according to past statistics.
Stats entered into the database will then be used to calculate the most even battle depending on three situations:

Handicap - you want to be one of your main characters and so does your oppenent. Well going into battle then we will
level the playing field by applying handicaps in the form of stocks. This way, both players have an almost even chance
of beating each other out.

Player Random -

Teams

"""
from .models import Stat, Character
from django.db.models import Sum
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import operator
from . import stats
'''
def Handicap():
    """
    Parameters: p1DR , p1KD, p1WL, p2DR, p2KD, p2WL
    :return: 
    """

def RandomPlayer()

    '''
def pnum_calc(user_string):
    user_stats = Stat.objects.filter(char_inst__user__username=user_string).filter().all()
    kd_dict = stats.kd_dict_maker(user_string)
    wl_dict = stats.wl_dict_maker(user_string)
    pnum_dict = {}
    for key, value in kd_dict.items():
        print(value)
        print(wl_dict[key])
        print(stats.dmg_ratio(user_string))
        pnum_dict[key] = value * wl_dict[key] * stats.dmg_ratio(user_string)
    return pnum_dict