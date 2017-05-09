from django.shortcuts import render, get_object_or_404

from .models import Character


# Create your views here.
def index(request):
    character_list = Character.objects.order_by('-initiative')
    context = {'character_list': character_list}
    return render(request, 'initiative/index.html', context)


def hero(request, hero_name):
    character = get_object_or_404(Character, name=hero_name)
    current_hp = character.hit_points - character.damage_taken
    return render(request, 'initiative/character.html',
                  {'character': character, 'current_hp': current_hp})
