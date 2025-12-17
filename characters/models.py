
from django.conf import settings
from django.db import models


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
        abilities = list(self.abilities.all().order_by('id'))
        if not abilities:
            self.current_ability = None
        elif self.current_ability not in abilities:
            self.current_ability = abilities[0]
        else:
            idx = abilities.index(self.current_ability)
            self.current_ability = abilities[(idx + 1) % len(abilities)]
        self.save()
        return self.current_ability

    def __str__(self):
        return f"{self.name} ({self.get_character_class_display()})"
