from django.urls import path
from .views import CharacterCreateView, CharacterListView, CharacterDetailView

urlpatterns = [
    path('create/', CharacterCreateView.as_view(), name='create_character'),
    path('', CharacterListView.as_view(), name='character_list'),  # default list view
    path("character/<int:pk>/", CharacterDetailView.as_view(), name="character_detail"),
]