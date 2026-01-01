# characters/admin.py
from django.contrib import admin
from .models import Ability, CharacterSheet, ClassAbility, CharacterToken

class CharacterTokenInline(admin.TabularInline):
    model = CharacterToken
    extra = 1  # how many empty forms to show by default
    autocomplete_fields = ['token']  # optional if you have many tokens

@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(ClassAbility)
class AbilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(CharacterSheet)
class CharacterSheetAdmin(admin.ModelAdmin):
    list_display = ('name', 'character_class', 'user', 'current_ability')
    search_fields = ('name', 'user__username')
    list_filter = ('character_class',)
    filter_horizontal = ('abilities',"class_abilities",)
    inlines = [CharacterTokenInline]  # <-- add this line
