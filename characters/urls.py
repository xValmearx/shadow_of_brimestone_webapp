from django.urls import path
from .views import CharacterCreateView, CharacterListView

urlpatterns = [
    path('create/', CharacterCreateView.as_view(), name='create_character'),
    path('', CharacterListView.as_view(), name='character_list'),  # default list view
]