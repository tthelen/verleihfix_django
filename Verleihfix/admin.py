# Register your models here.
from django.contrib import admin
from .models import Category, Type, Thing, Lending
from modeltranslation.admin import TranslationAdmin


class CategoryAdmin(TranslationAdmin):
    pass
class TypeAdmin(TranslationAdmin):
    pass
class ThingAdmin(TranslationAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Thing, ThingAdmin)
admin.site.register(Lending)
