from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import generic
from .models import Produkcje, Kategorie
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


class BaseView(generic.base.TemplateView):
    template_name = "base.html"
