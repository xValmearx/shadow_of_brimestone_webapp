# characters/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse


from .models import Ability, ClassAbility
from .forms import CharacterCreateForm
from .models import CharacterSheet, CLASS_DEFAULT_STATS

class CharacterCreateView(LoginRequiredMixin, FormView):

    # template name get the html page to use when creating a character
    template_name = 'characters/create_character.html'

    # get the form we are using when creating a new character,
    # this form only allows the user to select a character class, like marshall,gunslinger etc
    form_class = CharacterCreateForm


    # temp varible
    character = None

    # after a form is submitted
    def form_valid(self, form):

        # get the cleaned character class data from user
        char_class = form.cleaned_data['character_class']

        char_name = form.cleaned_data['character_name']

        # CLASS_DEFAULT_STATS has a BUNCH of info, it stores default classes and thier stats
        # marshall has a agility of 3, but gunslinger has agility of 6 for example

        # CLASS_DEFAULT_STATS = {
        # 'marshall':{
        #     'agility': 3,
        #     'cunning':4,
        #     },

        # 'gunslinger': {
        #     'agility': 6,
        #     'cunning':2,
        #     },
        #                     }
        


        # stats then gets the corresponding data dict based on the class
        stats = CLASS_DEFAULT_STATS.get(char_class, {})

        self.character = CharacterSheet.objects.create(
            user=self.request.user,
            character_class=char_class,
            name = char_name,

            # this stats function then automatically takes all the key word skills 
            # and assigns them into the correct data fields
            **stats
        )

        # Example: Marshall abilities
        if char_class == 'marshall':

            # get the set abilities for this character class
            ability_set = Ability.objects.filter(name__in=[
                "Hardend Resolve", "Rolling Thunder", "Cleaning Up The West"
            ])

            # set the filtered abilites
            self.character.abilities.set(ability_set)

            # set the current ability
            self.character.current_ability = ability_set.first()

            self.character.class_ability  = ClassAbility.objects.get(name__in=['Double Shot'])

            self.character.save()

        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the character list
        return reverse_lazy('character_list')
    
class CharacterListView(LoginRequiredMixin, ListView):
    model = CharacterSheet
    template_name = 'characters/character_list.html'
    context_object_name = 'characters'

    def get_queryset(self):

        # Only show characters belonging to the logged-in user
        return CharacterSheet.objects.filter(user=self.request.user)
    
class CharacterDetailView(DetailView):

    model = CharacterSheet
    template_name = "characters/character_detail.html"
    context_object_name = 'character'


    def post(self, request, *args, **kwargs):
        """
        Central POST manager for all character actions.
        Detects the action type and executes the corresponding method.
        """
        self.object = self.get_object()

        # Check authentication
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Not authenticated"}, status=403)

        # Check ownership
        if self.object.user != request.user:
            return JsonResponse({"error": "Not authorized"}, status=403)

        action = request.POST.get("action")

        if action == "cycle_ability":


            # the characters has a method to cycle to a new ability and return the new ability data
            # this cycle abiltiy also saves the ability state in the database as well
            # so if they user logges back in, current select ability will still be there
            new_ability = self.object.cycle_ability()
            
            # Handle case where there are no abilities
            if new_ability is None:
                return JsonResponse({
                    "type": "cycle_ability",
                    "new_ability_id": None,
                    "new_ability_name": None,
                    "new_ability_description": "No abilities available"
                })
            
            # the new ability also stores data about the new current select ability
            # the program returs this data to the front end to change the html
            return JsonResponse({
                "new_ability_name": new_ability.name,
                "new_ability_description": new_ability.description
            })
        
        if action == 'health':
            amount = int(request.POST.get('amount'))
            self.object.update_health(amount)

            return JsonResponse({
                "health": self.object.health,
                "max_health": self.object.max_health,
            })
        
        if action == 'sanity':
            amount = int(request.POST.get('amount'))
            self.object.update_sanity(amount)

            return JsonResponse({
                "sanity": self.object.sanity,
                "max_sanity": self.object.max_sanity,
            })
        
        if action == 'horror':
            amount = int(request.POST.get('amount'))
            self.object.update_horror(amount)

            return JsonResponse({
                "horror": self.object.horror,
                "max_horror": self.object.max_horror,
            })

        if action == 'grit':
            amount = int(request.POST.get('amount'))
            self.object.update_grit(amount)

            return JsonResponse({
                "grit": self.object.grit,
                "max_grit": self.object.max_grit,
            })
        # Handle unknown actions
        return JsonResponse({"error": "Unknown action"}, status=400)