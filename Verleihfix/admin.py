# Register your models here.
from django.contrib import admin

from .models import Thing, Lending

admin.site.register(Thing)
admin.site.register(Lending)
