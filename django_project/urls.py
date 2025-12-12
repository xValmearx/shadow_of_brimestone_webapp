
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


# local app imports

from characters.views import CharacterListView

def redirect_root(request):
    if request.user.is_authenticated:
        return redirect('character_list')   # <-- where logged-in users go
    return redirect('login')



urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('characters/', include('characters.urls')),
    path('', redirect_root),
    
    ]
    
