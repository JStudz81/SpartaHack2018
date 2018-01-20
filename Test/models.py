from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone



class GameTitle(models.Model):
    game_title = models.CharField(max_length=50)
    def __str__(self):
        return self.game_title


class Character(models.Model):

    name = models.CharField(max_length=30)

    game = models.ForeignKey(GameTitle, on_delete = models.CASCADE, related_name='characters')

    def __str__(self):
        return self.name



### INSTANCES ###

class CharInst(models.Model):
    #user_id from login

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='users')
    char = models.ForeignKey(Character, on_delete = models.CASCADE, related_name='char_insts')

    char_inst = [user, char]

    def __str__(self):
        #return self.user.username + ": " + self.char.name
        return self.char_inst


class Stat(models.Model):
    # FROM INSTANCE #

    # NULLABLES #
    wins = models.NullBooleanField(default=False)
    kills = models.PositiveIntegerField(default=0)
    deaths = models.PositiveIntegerField(default=0)
    damage_dealt = models.PositiveIntegerField(default=0)
    damage_received = models.PositiveIntegerField(default=0)
    char_inst = models.ForeignKey(CharInst, on_delete=models.CASCADE)
    time_stamp = timezone.now()