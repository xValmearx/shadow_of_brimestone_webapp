
from django.conf import settings
from django.db import models

from tokens.models import SaddleBagToken


CHARACTER_CLASSES = [
    ('marshall', 'Marshall'),
    ('gunslinger', 'Gunslinger'),
    ('rancher', 'Rancher'),
]


CLASS_DEFAULT_STATS = {
    'marshall': {
        # skills
        'agility': 3,
        'cunning':4,
        'spirit': 2,
        'strength': 2,
        'lore': 1,
        'luck':3,

        # combat skills
        'combat':2,
        'max_grit':2,
        'grit':2,
        "range":4,
        "melee":4,
        'initiative':4,

        # physical health
        'max_health': 10,
        'health':0,
        'defense': 3,
        'armor':0,

        # mental health
        'max_sanity': 10,
        'sanity':0,
        'will_power':4,
        'spirit_armor':0,

        # horror
        'max_horror':5,
        'horror':0,
        'corruption_resistance':0,

        },

    'gunslinger': {
        # skills
        'agility': 3,
        'cunning':4,
        'spirit': 2,
        'strength': 2,
        'lore': 1,
        'luck':3,

        # combat skills
        'combat':2,
        'max_grit':2,
        'grit':2,
        "range":4,
        "melee":4,
        'initiative':4,

        # physical health
        'max_health': 10,
        'health':0,
        'defense': 3,
        'armor':0,

        # mental health
        'max_sanity': 10,
        'sanity':0,
        'will_power':4,
        'spirit_armor':0,

        # horror
        'max_horror':5,
        'horror':0,
        'corruption_resistance':0,

        },

    'rancher': {
        # skills
        'agility': 3,
        'cunning':4,
        'spirit': 2,
        'strength': 2,
        'lore': 1,
        'luck':3,

        # combat skills
        'combat':2,
        'max_grit':2,
        'grit':2,
        "range":4,
        "melee":4,
        'initiative':4,

        # physical health
        'max_health': 10,
        'health':0,
        'defense': 3,
        'armor':0,

        # mental health
        'max_sanity': 10,
        'sanity':0,
        'will_power':4,
        'spirit_armor':0,

        # horror
        'max_horror':5,
        'horror':0,
        'corruption_resistance':0,

        },
}


class ClassAbility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Ability(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CharacterSheet(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )

    # character name
    name = models.CharField(max_length=100, blank=True, default="Unnamed Hero")

    character_class = models.CharField(
        max_length=50,
        choices=[('marshall', 'Marshall'), ('gunslinger', 'Gunslinger'), ('rancher', 'Rancher')]
    )

    # skills
    agility = models.IntegerField(default=0)
    cunning = models.IntegerField(default=0)
    spirit = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    lore = models.IntegerField(default=0)
    luck = models.IntegerField(default=0)

    # combat skills
    combat = models.IntegerField(default=0)
    max_grit = models.IntegerField(default=0)
    grit = models.IntegerField(default=0)
    range = models.IntegerField(default=0)
    melee = models.IntegerField(default=0)
    initiative = models.IntegerField(default=0)

    # physical health
    max_health = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    armor = models.IntegerField(default=0)

    # mental health
    max_sanity = models.IntegerField(default=0)
    sanity = models.IntegerField(default=0)
    will_power = models.IntegerField(default=0)
    spirit_armor = models.IntegerField(default=0)

    # horror
    max_horror = models.IntegerField(default=0)
    horror = models.IntegerField(default=0)
    corruption_resistance = models.IntegerField(default=0)

    # resources
    gold = models.IntegerField(default=0)
    dark_stone = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)

    class_ability = models.ForeignKey(
        ClassAbility,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )


    # abilities
    abilities = models.ManyToManyField(Ability, blank=True)

    current_ability = models.ForeignKey(
        Ability,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='active_for_characters'
    )

    # helper method to cycle abilities
    def cycle_ability(self):

        # make a list of all abilities orderd by ID
        abilities = list(self.abilities.all().order_by('id'))

        # if there are no abilities, set them to none
        if not abilities:
            self.current_ability = None

        elif self.current_ability not in abilities:
            self.current_ability = abilities[0]

        else:
            idx = abilities.index(self.current_ability)
            self.current_ability = abilities[(idx + 1) % len(abilities)]
        self.save()
        return self.current_ability

    def update_health(self,amount):

        if (self.health + amount) > self.max_health:
            return
        elif (self.health + amount) < 0:
            return 
        self.health += amount
        self.save()

    def update_sanity(self,amount):

        if (self.sanity + amount) > self.max_sanity:
            return
        elif (self.sanity + amount) < 0:
            return 
        self.sanity += amount
        self.save()

    def update_horror(self, amount):

        if (self.horror + amount) > self.max_horror:
            return
        elif (self.horror + amount) < 0:
            return

        self.horror += amount
        self.save()

    def update_grit(self, amount):

        if (self.grit + amount) > self.max_grit:
            return
        elif (self.grit + amount) < 0:
            return

        self.grit += amount
        self.save()

    def update_gold(self, amount):
        self.gold = max(0, self.gold + amount)
        self.save()

    def update_dark_stone(self, amount):
        self.dark_stone = max(0, self.dark_stone + amount)
        self.save()

    def update_xp(self, amount):
        self.xp = max(0, self.xp + amount)  # prevent negative XP
        self.save()


    def __str__(self):
        return f"{self.name} ({self.get_character_class_display()})"


# to get tokens in html, use {{character.tokens.all}}
class CharacterToken(models.Model):
    character = models.ForeignKey(
        CharacterSheet,
        on_delete=models.CASCADE,
        related_name='tokens'  # lets you access: character.tokens.all
    )

    token = models.ForeignKey(
        SaddleBagToken,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.character.name} - {self.token.name}"