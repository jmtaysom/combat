from django.contrib import admin

from .models import Player, Monster, MonsterList


admin.site.register(Player)
admin.site.register(Monster)
admin.site.register(MonsterList)
