# Register your models here.
from django.contrib import admin

from .models import Thing, Lending, Category, Type

admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Thing)
admin.site.register(Lending)
