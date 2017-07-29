from django.db import models
from django.core.validators import int_list_validator


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

    class Meta:
        abstract = False

    def __str__(self):
        return self.name

    def still_conscious(self):
        return self.hit_points - self.damage_taken >= 0


class Player(Character):
    present = models.BooleanField(default=True)


class Monster(Character):
    count = models.IntegerField(default=0)
    initiative_rolls = models.CharField(validators=[int_list_validator], max_length=50, default=0)


class MonsterList(models.Model):
    name = models.ForeignKey(Monster, on_delete=models.CASCADE)
    initiative = models.IntegerField(default=0)

    def __str__(self):
        return self.name


