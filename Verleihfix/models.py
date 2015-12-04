from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime


class Category(models.Model):
    """A category groups certain types."""
    name = models.CharField(max_length=80)
    icon = models.CharField(max_length=32)

    def types(self):
        return Type.objects.filter(category=self)

    def __str__(self):
        return self.name


class Type(models.Model):
    """A type is a set of identical thing instances."""
    name = models.CharField(max_length=80)
    category = models.ForeignKey(Category)
    description = models.TextField()
    image = models.ImageField()
    min_lending_span = models.IntegerField()
    max_lending_span = models.IntegerField()

    def things(self):
        return Thing.objects.filter(type=self)

    def available_things(self, startdate=None, enddate=None):
        return [x for x in self.things() if x.is_available(startdate, enddate)]

    def is_available(self, startdate=None, enddate=None):
        """Return number of things of this type that are available (now or for the given timespan)
           startdate: datetime object
           enddate: datetime object"""
        return len(self.available_things(startdate, enddate))

    def __str__(self):
        return self.name + " (" + self.category.name + ")"


class Thing(models.Model):
    """A thing is an instance of a type. It may have an additional description."""
    type = models.ForeignKey(Type)
    description = models.TextField()

    def is_available(self, startdate=None, enddate=None):
        if not startdate:
            startdate = date.today()
        if not enddate:
            enddate = date.today()
        overlapping = self.lending_set.filter(status__in=['l','r']).filter(start__lte = startdate, end__gte = enddate)
        return overlapping.count() == 0

    def lend(self, user, startdate, enddate, status='r'):
        if self.is_available(startdate, enddate):
            l = Lending(thing=self, user=user, start=startdate, end=enddate, status=status)
            l.save()
            # TODO: check for overlaps!
            return True
        else:
            return False

    def __str__(self):
        return "An instance of "+self.type.name


class Lending(models.Model):
    """A lending of a thing."""
    STATES = (('r', 'Reserviert'), ('l', 'Ausgeliehen'), ('x', 'Zurückgegeben'), ('o', 'Storniert'))
    thing = models.ForeignKey(Thing)
    user = models.ForeignKey(User)
    start = models.DateField()
    end = models.DateField()
    status = models.CharField(max_length=1, choices=STATES)
