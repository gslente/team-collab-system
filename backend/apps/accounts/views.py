from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class UserLoginView(TemplateView):
    template_name = 'accounts/user_login.html'
