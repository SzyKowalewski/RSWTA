from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import generic
from .models import Produkcje, Kategorie


def widok_home(request):
    kategorie = Kategorie.objects.all()
    filmy = Produkcje.objects.all()
    return render(request, 'home.html', {'filmy': filmy, 'kategorie': kategorie})


class BaseView(generic.base.TemplateView):
    template_name = "base.html"
