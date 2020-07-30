from django.shortcuts import render

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutCreatorView(TemplateView):
    template_name = 'AboutMe.html'
