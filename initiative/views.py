from django.shortcuts import render
from django.http import HttpResponse

from .models import Character

# Create your views here.
def index(request):
    character_list = Character.objects.order_by('-initiative')
    context = {'character_list': character_list}
    return render(request, 'initiative/index.html', context)


def hero(request, hero_name):
    response = f'{hero_name}'
    return HttpResponse(response)
