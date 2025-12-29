# characters/forms.py
from django import forms

# app imports
from .models import CHARACTER_CLASSES
from tokens.models import SaddleBagToken

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
    

class AddCharacterTokenForm(forms.Form):
    token = forms.ModelChoiceField(
        queryset=SaddleBagToken.objects.all(),
        label="Select Saddle Bag Token",
        empty_label="-- Choose a token --"
    )
