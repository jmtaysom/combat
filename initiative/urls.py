from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /initiative/
    url(r'^$', views.index, name='index'),
    # ex: /iniative/Marius/
    url(r'^(?P<hero_name>[\w\s]+)/$', views.hero, name='hero'),
    url(r'^(?P<hero_name>[\w\s]+)/update/$', views.update, name='update'),
    #url(r'^(?P/update/<hero_name>[\w\s]+/$', views.update_form, name='update_character'),
]