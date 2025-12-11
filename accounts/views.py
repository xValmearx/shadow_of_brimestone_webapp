from django.contrib.auth import login
from django.urls import reverse_lazy
from django.shortcuts import redirect  
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # auto-login after signup
        return redirect(self.success_url)