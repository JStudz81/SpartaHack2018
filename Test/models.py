from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class Character(models.Model):

    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name

    game = models.ForeignKey('GameTitle', on_delete = models.CASCADE)

class GameTitle(models.Model):
    game_title = models.CharField(max_length=50)
    def __str__(self):
        return self.game_title

### INSTANCES ###

class CharInst(models.Model):
    #user_id from login

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    char = models.ForeignKey(Character, on_delete = models.CASCADE)


    def __str__(self):
        return self.user.username + ": " + self.char.name

    game = models.ForeignKey(GameTitle, on_delete=models.CASCADE)


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