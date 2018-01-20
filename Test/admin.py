

from django.contrib import admin

from .models import Character
from .models import CharInst
from .models import Stat
from .models import GameTitle

admin.site.register(Character)
admin.site.register(CharInst)
admin.site.register(GameTitle)
admin.site.register(Stat)