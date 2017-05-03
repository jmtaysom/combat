from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /initiative/
    url(r'^$', views.index, name='index'),
    # ex: /iniative/Marius/
    url(r'^(?P<hero_name>[A-Za-z]+)/$', views.hero, name='hero'),
]