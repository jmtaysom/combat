from itertools import chain
from operator import attrgetter
from copy import deepcopy

from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory

from .forms import CharacterForm, CountForm, CharacterCountForm, MonsterForm
from .models import Player, Monster


# Create your views here.
def index(request):
    #TODO: allow for the removal of characters or monsters with a click of a button
    character_list = Player.objects.filter(present=True).order_by('-initiative')
    monster_list = Monster.objects.filter(count__gt=0)
    multiple_monsters = []
    for monster in monster_list:
        for init in monster.initiative_rolls.split(','):
            m = deepcopy(monster)
            m.is_monster = True
            m.initiative = int(init)
            multiple_monsters.append(m)
    result_list = sorted(
        chain(character_list, multiple_monsters),
        key=attrgetter('initiative'),
        reverse=True)
    context = {'character_list': result_list}
    return render(request, 'initiative/index.html', context)


def characters(request):
    CharacterFormSet = modelformset_factory(Player, extra=0, form=CharacterCountForm)
    if request.method == 'POST':
        formset = CharacterFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        formset = CharacterFormSet(queryset=Player.objects.all())

    return render(request, 'initiative/character_list.html', {'formset': formset})


def monsters(request):
    #TODO: add in handling for monster initiative. Something that also allows for removal of the monsters one at a time.
    CharacterFormSet = modelformset_factory(Monster, extra=0, form=CountForm)
    if request.method == 'POST':
        formset = CharacterFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        formset = CharacterFormSet(queryset=Monster.objects.all())

    return render(request, 'initiative/monster_list.html', {'formset': formset})


def hero(request, hero_name):
    # TODO: combine views for characters and monsters again.
    character = get_object_or_404(Player, name=hero_name)
    current_hp = character.hit_points - character.damage_taken
    return render(request, 'initiative/character.html',
                  {'character': character, 'current_hp': current_hp})


def monster_detail(request, monster_name):
    monster = get_object_or_404(Monster, name=monster_name)
    current_hp = monster.hit_points - monster.damage_taken
    return render(request, 'initiative/character.html',
                  {'character': monster, 'current_hp': current_hp})


def update(request, hero_name):
    character = get_object_or_404(Player, name=hero_name)
    if request.method == "POST":
        form = CharacterForm(request.POST, instance=character)
    else:
        form = CharacterForm(instance=character)
    if form.is_valid():
        form.save()
    return render(request, 'initiative/update.html', {'form':form})


def monster_update(request, monster_name):
    monster = get_object_or_404(Monster, name=monster_name)
    if request.method == "POST":
        form = MonsterForm(request.POST, instance=monster)
    else:
        form = MonsterForm(instance=monster)
    if form.is_valid():
        form.save()
    return render(request, 'initiative/update.html', {'form':form})


def initiative(request, hero_name, init):
    character = get_object_or_404(Player, name=hero_name)
    character.initiative = init
    character.save()
    return redirect(f'/characters/{hero_name}/')