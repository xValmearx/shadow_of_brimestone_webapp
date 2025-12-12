# characters/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import CharacterCreateForm
from .models import CharacterSheet, CLASS_DEFAULT_STATS

class CharacterCreateView(LoginRequiredMixin, FormView):
    template_name = 'characters/create_character.html'
    form_class = CharacterCreateForm

    character = None

    def form_valid(self, form):
        char_class = form.cleaned_data['character_class']

        stats = CLASS_DEFAULT_STATS.get(char_class, {})

        self.character = CharacterSheet.objects.create(
            user=self.request.user,
            character_class=char_class,
            **stats
        )

        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the character list instead of an edit page
        return reverse_lazy('character_list')
    
class CharacterListView(LoginRequiredMixin, ListView):
    model = CharacterSheet
    template_name = 'characters/character_list.html'
    context_object_name = 'characters'

    def get_queryset(self):
        # Only show characters belonging to the logged-in user
        return CharacterSheet.objects.filter(user=self.request.user)