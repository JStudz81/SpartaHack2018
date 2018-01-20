from . import models


def most_kills(char_or_user):
    """
    Parameters: Enter either a char or user query set
    Returns the collection of objects that have the highest number of kills
    """

    sp_col = models.Stat.objects.filter(char_or_user)

    for character in sp_col:
        max_kills = 0
        max_kills += 1
    max_kills = sp_col.aggregate(Max('kills'))
    max_kills_col = specific_col.all(kills = max_kills)

    return max_kills_col


def num_wins(char_or_user):
    sp_col = Stat.objects.select_related(char_or_user)
    num_wins = sp_col.aggregate(Count(wins=True))
    return num_wins

