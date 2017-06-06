from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /characters/
    url(r'^characters/$', views.characters, name='characters'),
    # ex: /characters/
    url(r'^monsters/$', views.monsters, name='monsters'),
    # ex: /Marius/
    url(r'^characters/(?P<hero_name>[\w\s]+)/$', views.hero, name='hero'),
    url(r'^characters/(?P<hero_name>[\w\s]+)/update/$', views.update, name='update'),

]