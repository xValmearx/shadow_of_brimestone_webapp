# characters/forms.py
from django import forms
from .models import CHARACTER_CLASSES

class CharacterCreateForm(forms.Form):

    character_name = forms.CharField(
        max_length=50,
        label="Character Name",
        widget=forms.TextInput(attrs={
            "placeholder": "Enter character name"
        })
    )

    character_class = forms.ChoiceField(
        choices=CHARACTER_CLASSES, 
        label="Select Character Class"
        )
