# characters/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


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

            # this stats function then automatically takes all the key word skills 
            # and assigns them into the correct data fields
            **stats
        )

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
    
