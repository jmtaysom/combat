from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=50)
    initiative = models.IntegerField()
    armor_class = models.IntegerField()
    fortitude = models.IntegerField()
    reflex = models.IntegerField()
    will = models.IntegerField()
    hit_points = models.IntegerField()
    notes = models.CharField(max_length=200)

    
