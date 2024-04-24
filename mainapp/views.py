from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import generic


class HomeView(generic.base.TemplateView):
    template_name = "home.html"
