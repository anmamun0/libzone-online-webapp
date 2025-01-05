from django.shortcuts import render , redirect
from django.views.generic import CreateView , FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout

from django.urls import reverse_lazy
# Create your views here.
from .forms import RegistraionForm 
from django.contrib.auth.views import LoginView

class RegistrationView(FormView):
    template_name = 'accounts/registration.html'
    form_class = RegistraionForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    def get_success_url(self):
        return reverse_lazy('home')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request) 
    return redirect('login')