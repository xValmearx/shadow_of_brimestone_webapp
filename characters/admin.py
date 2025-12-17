# characters/admin.py
from django.contrib import admin
from .models import Ability, CharacterSheet

@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(CharacterSheet)
class CharacterSheetAdmin(admin.ModelAdmin):
    list_display = ('name', 'character_class', 'user', 'current_ability')
    search_fields = ('name', 'user__username')
    list_filter = ('character_class',)
    filter_horizontal = ('abilities',)
