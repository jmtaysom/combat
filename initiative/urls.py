from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /initiative/
    url(r'^$', views.index, name='index'),
    # ex: /iniative/Marius/
    url(r'^(?P<hero_name>[\w\s]+)/$', views.hero, name='hero'),
]