from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=30)
    #game_id = models.ForeignKey('GameTitle', on_delete = models.CASCADE)

#class GameTitle(models.Model):
    #game_title = models.Model(max_length=50)

### INSTANCES ###

class CharInst(models.Model):
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)
    #game_id = models.ForeignKey('GameTitle', on_delete=models.CASCADE)

"""
class Stat(models.Model):
    # FROM INSTANCE #
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    game_id = models.ForeignKey('GameTitle', on_delete=models.CASCADE)

    # NULLABLES #
    wins = 
    losses =
    kills =
    deaths =
    damage_dealt =
    damage_received =
"""