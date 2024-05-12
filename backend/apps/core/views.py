from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
'''
View model that defines a singular login URL for all other views
Inherit this View if View requires login
'''
class LoginRequiredView(LoginRequiredMixin):
    login_url = '/user/login/'

class CallToActionHomeView(TemplateView, LoginRequiredMixin):
    template_name = 'cta/home__cta.html'

class HomeView(LoginRequiredView, TemplateView):
    template_name = 'home.html'
