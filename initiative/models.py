from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=50)
    initiative = models.IntegerField()
    armor_class = models.IntegerField()
    fortitude = models.IntegerField()
    reflex = models.IntegerField()
    will = models.IntegerField()
    hit_points = models.IntegerField()
    damage_taken = models.IntegerField(default=0)
    notes = models.CharField(max_length=200, blank=True)
    unique = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def still_conscious(self):
        return self.hit_points >= 0
