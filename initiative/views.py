from django.shortcuts import render, get_object_or_404
from django.forms import modelformset_factory

from .forms import CharacterForm, CountForm, CharacterCountForm
from .models import Character


# Create your views here.
def index(request):
    character_list = Character.objects.order_by('-initiative')
    character_list_count = []
    for character in character_list:
        for i in range(character.count):
            character_list_count.append(character)
    context = {'character_list': character_list_count}
    return render(request, 'initiative/index.html', context)


def characters(request):
    CharacterFormSet = modelformset_factory(Character, extra=0, form=CharacterCountForm)
    if request.method == 'POST':
        formset = CharacterFormSet(request.POST, request.FILES)
    else:
        formset = CharacterFormSet(queryset=Character.objects.filter(unique=True))
    if formset.is_valid():
        formset.save()
    return render(request, 'initiative/character_list.html', {'formset': formset})


def monsters(request):
    CharacterFormSet = modelformset_factory(Character, extra=0, form=CountForm)
    if request.method == 'POST':
        formset = CharacterFormSet(request.POST, request.FILES)
        print(request.POST)
    else:
        formset = CharacterFormSet(queryset=Character.objects.filter(unique=False))
    if formset.is_valid():
        formset.save()
    return render(request, 'initiative/character_list.html', {'formset': formset})


def hero(request, hero_name):
    character = get_object_or_404(Character, name=hero_name)
    current_hp = character.hit_points - character.damage_taken
    return render(request, 'initiative/character.html',
                  {'character': character, 'current_hp': current_hp})

def update(request, hero_name):
    character = get_object_or_404(Character, name=hero_name)
    if request.method == "POST":
        form = CharacterForm(request.POST, instance=character)
    else:
        form = CharacterForm(instance=character)
    if form.is_valid():
        form.save()
    return render(request, 'initiative/update.html', {'form':form})
