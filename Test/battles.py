
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


from Test.models import *
from Test.stats import *
from .models import Stat, Character
from . import stats
import random


def handicap(p1,c1,p2,c2):
    """
    Parameters: p1DR , p1KD, p1WL, p2DR, p2KD, p2WL
    (p1 is person on the left, p2 is person on the right)
    :return: Relative Handicap
    """

    p1DB = dmg_per_kill(p1)
    p1DA = dmg_per_death(p1)
    p1KD = kd_ratio(c1, p1)
    p1WL = wl_ratio(p1)
    p2DB = dmg_per_kill(c2)
    p2DA = dmg_per_death(p2)
    p2KD = kd_ratio(c2, p2)
    p2WL = wl_ratio(p2)
    
    return [round(0.5*p2KD/p1KD*abs(p2DB/p1DB - p2DA/p1DA)**(1/p1WL)), round(0.5*p1KD/p2KD*abs(p1DB/p2DB - p1DA/p2DA))**(1/p2WL)]


def pnum_calc(user_string):
    user_stats = Stat.objects.filter(char_inst__user__username=user_string).filter().all()
    kd_dict = stats.kd_dict_maker(user_string)
    wl_dict = stats.wl_dict_maker(user_string)
    pnum_dict = {}
    for key, value in kd_dict.items():
        #print(value)
        #print(wl_dict[key])
        #print(stats.dmg_ratio(user_string))
        pnum_dict[key] = value * wl_dict[key] * stats.dmg_ratio(user_string)
    return pnum_dict


def match_finder(user_string1, user_string2):

    length = 10

    pnum1 = pnum_calc(user_string1)
    pnum2 = pnum_calc(user_string2)

    for r in range(7):
        c = random.choice(pnum1.keys())
        random.choice(list(pnum1.items()))

        d = random.choice(pnum2.keys())
        random.choice(list(pnum2.items()))

        if abs(c[1]-d[1]) < length:
            a=c
            b=d
            length = abs(b[1]-a[1])
        else:
            continue


    return(a[0],b[0])