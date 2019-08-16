from django.db import models

# Create your models here.
class Enemy(models.Model):
    hp = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    appear_field = models.IntegerField(default=0)
    xp_gain = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Player(models.Model):
    hp = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    time_spent = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=0)

class Leveling(models.Model):
    Level=models.IntegerField(default=0)
    Xp_required=models.IntegerField(default=0)

class Field(models.Model):
    name= models.CharField(max_length=15)

    
    def __str__(self):
        return self.name