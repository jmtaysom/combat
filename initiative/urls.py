from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /characters/
    url(r'^characters/$', views.characters, name='characters'),
    # ex: /Marius/
    url(r'^(?P<hero_name>[\w\s]+)/$', views.hero, name='hero'),
    url(r'^(?P<hero_name>[\w\s]+)/update/$', views.update, name='update'),

]