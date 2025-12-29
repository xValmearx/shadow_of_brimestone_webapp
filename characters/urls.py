from django.urls import path
from .views import CharacterCreateView, CharacterListView, CharacterDetailView,AddTokenToCharacterView

urlpatterns = [
     path(
        "character/<int:character_pk>/add-token/",
        AddTokenToCharacterView.as_view(),
        name="add_token_to_character"
    ),
    path("character/<int:pk>/",
          CharacterDetailView.as_view(), 
          name="character_detail"
    ),
    path('create/', 
         CharacterCreateView.as_view(), 
         name='create_character'
    ),
    path('', 
         CharacterListView.as_view(), 
         name='character_list'
    ),  # default list view
]