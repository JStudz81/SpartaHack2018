from .models import Stat, Character
from django.db.models import Sum
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import operator



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


def kd_avg():
    # average kd over all characters (weighted according to play)
    m = Stat.objects.all()
    kills = m.aggregate(Sum('kills'))
    deaths = m.aggregate(Sum('deaths'))
    kills = kills['kills__sum']
    deaths = deaths['deaths__sum']
    return round(kills/deaths, 3)


def kd_rank(user_id):
    m = User.objects.all()

    rank = {}
    print('havent broken', m)

    for n in m:
        print(n)
        rank[n.username] = Stat.objects.filter(char_inst__user_id=user_id).count()

    sorted_list = sorted(rank.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_list


'''
Calculates total amount of wins per user of character
'''
def num_wins(char_or_user):

    if temp_search(char_or_user) == True:
        char = Character.objects.get(name=char_or_user)
        n = Stat.objects.filter(char_inst__char_id=char.id).all()
        num_wins = n.aggregate(Sum('wins'))
        num_wins = num_wins['wins__sum']
        if not num_wins:
            return 0
        return num_wins

    else:
        user = User.objects.get(username=char_or_user)
        n = Stat.objects.filter(char_inst__user_id=user.id).all()
        num_wins = n.aggregate(Sum('wins'))
        num_wins = num_wins['wins__sum']
        if not num_wins:
            return 0
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
        if not num_wins:
            return 0
        num_losses = n.count() - num_wins
        if num_losses < 1:
            return num_wins
        return (num_wins/num_losses)


    else:
        user = User.objects.get(username=char_or_user)
        n = Stat.objects.filter(char_inst__user_id=user.id).all()
        num_wins = n.aggregate(Sum('wins'))
        num_wins = num_wins['wins__sum']
        if not num_wins:
            return 0
        num_losses = n.count() - num_wins
        if num_losses < 1:
            return num_wins
        return (num_wins/num_losses)


def dmg_ratio(char_or_user):
    if temp_search(char_or_user):
        char = Character.objects.get(name=char_or_user)
        n = Stat.objects.filter(char_inst__char_id=char.id).all()
        dmg_given = n.aggregate(Sum('damage_dealt'))
        dmg_given = dmg_given['damage_dealt__sum']
        dmg_taken = n.aggregate(Sum('damage_received'))
        dmg_taken = dmg_taken['damage_received__sum']
        if dmg_taken < 1:
            return dmg_given
        return round(dmg_given/dmg_taken, 3)
    else:
        user = User.objects.get(username=char_or_user)
        n = Stat.objects.filter(char_inst__user_id=user.id).all()
        dmg_given = n.aggregate(Sum('damage_dealt'))
        dmg_given = dmg_given['damage_dealt__sum']
        dmg_taken = n.aggregate(Sum('damage_received'))
        dmg_taken = dmg_taken['damage_received__sum']
        if dmg_taken < 1:
            return dmg_given
        return round(dmg_given/dmg_taken, 3)

def dmg_per_kill(char_or_user):
    if temp_search(char_or_user):
        char = Character.objects.get(name=char_or_user)
        n = Stat.objects.filter(char_inst__char_id=char.id).all()
        dmg_given = n.aggregate(Sum('damage_dealt'))
        dmg_given = dmg_given['damage_dealt__sum']
        kills = n.aggregate(Sum('kills'))
        kills = kills['kills__sum']
        if kills < 1:
            return dmg_given
        return round(dmg_given/kills, 3)
    else:
        user = User.objects.get(username=char_or_user)
        n = Stat.objects.filter(char_inst__user_id=user.id).all()
        dmg_given = n.aggregate(Sum('damage_dealt'))
        dmg_given = dmg_given['damage_dealt__sum']
        kills = n.aggregate(Sum('kills'))
        kills = kills['kills__sum']
        if kills < 1:
            return dmg_given
        return round(dmg_given/kills, 3)

def dmg_per_death(char_or_user):
    if temp_search(char_or_user):
        char = Character.objects.get(name=char_or_user)
        n = Stat.objects.filter(char_inst__char_id=char.id).all()
        dmg_taken = n.aggregate(Sum('damage_received'))
        dmg_taken = dmg_taken['damage_received__sum']
        deaths = n.aggregate(Sum('deaths'))
        deaths = deaths['deaths__sum']
        if deaths < 1:
            return dmg_taken
        return round(dmg_taken/deaths, 3)
    else:
        user = User.objects.get(username=char_or_user)
        n = Stat.objects.filter(char_inst__user_id=user.id).all()
        dmg_taken = n.aggregate(Sum('damage_received'))
        dmg_taken = dmg_taken['damage_received__sum']
        deaths = n.aggregate(Sum('deaths'))
        deaths = deaths['deaths__sum']
        if deaths < 1:
            return dmg_taken
        return round(dmg_taken / deaths, 3)


def rank(user_id):
    chars = Character.objects.filter(char_insts__user_id=user_id).all()

    rank = {}

    for char in chars:
        rank[char.name] = Stat.objects.filter(char_inst__char_id=char.id).count()

    sorted_list = sorted(rank.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_list




def total_games(user_string):
    # all the times the user has played
    user = Stat.objects.filter(char_inst__user__username=user_string).all()
    return user.count()


'''
returns a dictionary with the character id's as keys and the k/d ratio as values
'''
def kd_dict_maker(user_string):
    user_stats = Stat.objects.filter(char_inst__user__username=user_string).filter().all()
    kills_dict = {}
    for stat in user_stats:
        if stat.char_inst.char.id not in kills_dict:
            kills_dict[stat.char_inst.char.id] = [stat.kills, stat.deaths]
        else:
            kills_dict[stat.char_inst.char.id][0] += stat.kills
            kills_dict[stat.char_inst.char.id][1] += stat.deaths
    for key, value in kills_dict.items():
        if(value[1] != 0):
            kills_dict[key] = round(value[0]/value[1], 3)
        else:
            kills_dict[key] = value[0]
    return kills_dict

'''
returns a dictionary with the character id's as keys and the w/l ratio as values
'''
def wl_dict_maker(user_string):
    user_stats = Stat.objects.filter(char_inst__user__username=user_string).filter().all()
    wins_dict = {}
    for stat in user_stats:
        if stat.char_inst.char.id not in wins_dict:
            wins_dict[stat.char_inst.char.id] = [int(stat.wins), int(not stat.wins)]

        else:
            wins_dict[stat.char_inst.char.id][0] += int(stat.wins)
            wins_dict[stat.char_inst.char.id][1] += int(not stat.deaths)
    for key, value in wins_dict.items():
        if(value[1] != 0):
            wins_dict[key] = round(value[0]/value[1], 3)
        else:
            wins_dict[key] = value[0]
    return wins_dict

'''
returns the highest kd for a users character, and the id of the character(s) that has the kd.
'''
def best_kd(kills_dict):
    max_value = max(kills_dict.values())  # maximum value
    max_keys = [k for k, v in kills_dict.items() if v == max_value]
    return (max_value, max_keys)

'''
returns the highest wl for a users character, and the id of the character(s) that has the wl.
'''
def best_wl(wins_dict):
    max_value = max(wins_dict.values())  # maximum value
    max_keys = [k for k, v in wins_dict.items() if v == max_value]
    return (max_value, max_keys)

