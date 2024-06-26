from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    type_1 = models.CharField(max_length=255)
    type_2 = models.CharField(max_length=255, blank=True, null=True)
    total = models.IntegerField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_atk = models.IntegerField()
    sp_def = models.IntegerField()
    speed = models.IntegerField()
    generation = models.IntegerField()
    legendary = models.BooleanField()
