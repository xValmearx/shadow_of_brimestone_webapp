# characters/forms.py
from django import forms
from .models import CHARACTER_CLASSES

class CharacterCreateForm(forms.Form):
    character_class = forms.ChoiceField(choices=CHARACTER_CLASSES, label="Select Character Class")
