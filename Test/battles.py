
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

def Handicap(p1, c1, p2, c2):
    """
    Parameters: p1DR , p1KD, p1WL, p2DR, p2KD, p2WL
    (p1 is person on the left, p2 is person on the right)
    :return: Relative Handicap
    """

    p1DB = dmg_per_kill(p1)
    p1DA = dmg_per_death(p1)
    p1KD = kd_ratio(p1, c1)
    p1WL = wl_ratio(p1)
    p2DB = dmg_per_kill(p2)
    p2DA = dmg_per_death(p2)
    p2KD = kd_ratio(p2, c2)
    p2WL = wl_ratio(p2)
    
    return np.round([p2KD/p1KD*abs(p2DB/p1DB - p2DA/p1DA)**(1/p1WL), p1KD/p2KD*abs(p1DB/p2DB - p1DA/p2DA)**(1/p2WL)])



def RandomPlayer():
    pass
