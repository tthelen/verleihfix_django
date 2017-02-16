from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Type, Thing


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class TypeTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


class ThingTranslationOptions(TranslationOptions):
    fields = ('description',)


translator.register(Category, CategoryTranslationOptions)
translator.register(Type, TypeTranslationOptions)
translator.register(Thing, ThingTranslationOptions)