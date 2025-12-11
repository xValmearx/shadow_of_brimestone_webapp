from django.views.generic import TemplateView

# Create your views here.





class DashBoardView(TemplateView):
    """Dash Board view"""

    template_name = 'home.html'