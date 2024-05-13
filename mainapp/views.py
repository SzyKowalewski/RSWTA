from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views import generic
from .models import Produkcje, Kategorie, Rezencje, Uzytkownicy
from django.db.models import Q
from django.contrib.auth import authenticate, login



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


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = Uzytkownicy.objects.get(E_mail=email)
        except Uzytkownicy.DoesNotExist:
            user = None
        if user is not None and user.Haslo == password:
            request.session['user_id'] = user.id
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Nieprawidłowe dane logowania'})
    else:
        return render(request, 'login.html')


def register_view(request):

    return render(request, 'register.html')


class BaseView(generic.base.TemplateView):
    template_name = "base.html"
