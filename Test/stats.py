from .models import Stat, Character
from django.db.models import Sum
from django.contrib.auth.models import User



def total_kills(char_or_user):

    char = Character.objects.get(name=char_or_user)

    if char:
        n = Stat.objects.filter(char_inst__char_id=char.id).all()
        kills = n.aggregate(Sum('kills'))
        return kills

    user = User.objects.get(username=char_or_user)

    if user:
        n = Stat.objects.filter(char_inst__user_id=user.id).all()
        kills = n.aggregate(Sum('kills'))
        return kills

### JASON'S WIN FUNCTION ###
