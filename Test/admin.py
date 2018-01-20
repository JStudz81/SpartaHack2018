from django.contrib import admin

from .models import User
from .models import Character
from .models import CharInst

admin.site.register(User)
admin.site.register(Character)
admin.site.register(CharInst)