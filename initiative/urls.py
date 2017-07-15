from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /characters/
    url(r'^characters/$', views.characters, name='characters'),
    # ex: /characters/
    url(r'^monsters/$', views.monsters, name='monsters'),
    # ex: /characters/Marius/
    url(r'^characters/(?P<hero_name>[\w\s]+)/$', views.hero, name='hero'),

    url(r'^monsters/(?P<monster_name>[\w\s]+)/$', views.monster_detail, name='monster_detail'),
    # ex: /characters/Marius/15/
    url(r'^characters/(?P<hero_name>[\w\s]+)/(?P<init>[0-9]+)/$', views.initiative, name='hero'),
    # ex: /characters/Marius/update/
    url(r'^characters/(?P<hero_name>[\w\s]+)/update/$', views.update, name='update'),
    url(r'^monsters/(?P<monster_name>[\w\s]+)/update/$', views.monster_update, name='monster_update'),
    url(r'^monster_list/$', views.monster_list, name='monster_list'),

]