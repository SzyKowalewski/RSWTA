from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import generic
from .models import Produkcje, Kategorie, Rezencje, Uzytkownicy
from django.db.models import Q


def widok_home(request):
    kategorie = Kategorie.objects.all()
    filmy = Produkcje.objects.all()

    wybrana_kategoria = request.GET.get('kategoria')
    wpisana_fraza = request.GET.get('fraza')

    if wybrana_kategoria:
        filmy = filmy.filter(ID_Kategorii=wybrana_kategoria)

    if wpisana_fraza:
        filmy = filmy.filter(Q(Tytul__icontains=wpisana_fraza) | Q(Rezyser__icontains=wpisana_fraza))

    return render(request, 'home.html', {'filmy': filmy, 'kategorie': kategorie})


def details_view(request):
    filmy = Produkcje.objects.all()
    opinie = Rezencje.objects.all()
    uzytkownicy = Uzytkownicy.objects.all()

    return render(request, 'movie_info.html', {'filmy': filmy, 'opinie': opinie, 'uzytkownicy': uzytkownicy})


class BaseView(generic.base.TemplateView):
    template_name = "base.html"
