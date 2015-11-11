from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField()
    min_lending_span = models.IntegerField()
    max_lending_span = models.IntegerField()

    def is_available(self):
        overlapping = self.lending_set.filter(start__lte = date.today(), end__gte = date.today())
        return overlapping.count() == 0

class Lending(models.Model):
    STATES = (('r', 'reserved'), ('l', 'lended'))
    thing = models.ForeignKey(Thing)
    user = models.ForeignKey(User)
    start = models.DateField()
    end = models.DateField()
    status = models.CharField(max_length=1, choices=STATES)
