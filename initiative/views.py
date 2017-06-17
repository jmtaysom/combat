from itertools import chain
from operator import attrgetter
from random import randint
from copy import deepcopy

from django.shortcuts import render, get_object_or_404
from django.forms import modelformset_factory

from .forms import CharacterForm, CountForm, CharacterCountForm
from .models import Player, Monster


# Create your views here.
def index(request):
    character_list = Player.objects.filter(present=True).order_by('-initiative')
    monster_list = Monster.objects.filter(count__gt=0)
    multiple_monsters = []
    for monster in monster_list:
        for init in monster.initiative_rolls.split(','):
            m = deepcopy(monster)
            m.initiative = int(init)
            multiple_monsters.append(m)
    result_list = sorted(
        chain(character_list, multiple_monsters),
        key=attrgetter('initiative'),
        reverse=True)
    print(character_list)
    context = {'character_list': result_list}
    return render(request, 'initiative/index.html', context)


def characters(request):
    CharacterFormSet = modelformset_factory(Player, extra=0, form=CharacterCountForm)
    if request.method == 'POST':
        formset = CharacterFormSet(request.POST, request.FILES)
    else:
        formset = CharacterFormSet(queryset=Player.objects.all())
    if formset.is_valid():
        formset.save()
    return render(request, 'initiative/character_list.html', {'formset': formset})


def monsters(request):
    CharacterFormSet = modelformset_factory(Monster, extra=0, form=CountForm)
    if request.method == 'POST':
        formset = CharacterFormSet(request.POST, request.FILES)
    else:
        formset = CharacterFormSet(queryset=Monster.objects.all())
    if formset.is_valid():
        formset.save()
    return render(request, 'initiative/monster_list.html', {'formset': formset})


def hero(request, hero_name):
    character = get_object_or_404(Player, name=hero_name)
    current_hp = character.hit_points - character.damage_taken
    return render(request, 'initiative/character.html',
                  {'character': character, 'current_hp': current_hp})

def update(request, hero_name):
    character = get_object_or_404(Player, name=hero_name)
    if request.method == "POST":
        form = CharacterForm(request.POST, instance=character)
    else:
        form = CharacterForm(instance=Player)
    if form.is_valid():
        form.save()
    return render(request, 'initiative/update.html', {'form':form})
