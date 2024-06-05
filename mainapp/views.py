from django.contrib.auth.models import User
from django.http import Http404

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Produkcje, Kategorie, Rezencje, Uzytkownicy, Do_obejrzenia, Obejrzane
from django.db.models import Q
from django.contrib.auth import logout


def widok_home(request):
    kategorie = Kategorie.objects.all()
    filmy = Produkcje.objects.all()

    wybrana_kategoria = request.GET.get('kategoria')
    wpisana_fraza = request.GET.get('fraza')

    if wybrana_kategoria:
        filmy = filmy.filter(ID_Kategorii=wybrana_kategoria)

    if wpisana_fraza:
        filmy = filmy.filter(Q(Tytul__icontains=wpisana_fraza) | Q(Rezyser__icontains=wpisana_fraza))

    user = request.user  # Pobieramy użytkownika z requestu
    return render(request, 'home.html', {'filmy': filmy, 'kategorie': kategorie, 'user': user})


def details_view(request, film_id):
    try:
        film = get_object_or_404(Produkcje, id=film_id)
    except Http404:
        return render(request, 'missing_data.html', {'data': "film"})
    else:
        opinie = Rezencje.objects.filter(ID_Produkcji_id=film_id)
        uzytkownicy = Uzytkownicy.objects.all()

        if request.method == 'POST':
            score = request.POST['score']
            comment = request.POST['comment']
            id_produkcji = request.POST['id_produkcji']
            id_uzytkownika = request.POST['id_uzytkownika']
            if int(score) > 10 or int(score) < 0:
                user = request.user
                return render(request, 'movie_info.html',
                              {'film': film, 'opinie': opinie, 'uzytkownicy': uzytkownicy, 'user': user, 'error': 'Ocena musi być z zakresu 0 a 10'})
            review = Rezencje.objects.create(Ocena=score, Komentarz=comment, ID_Produkcji_id=id_produkcji, ID_Uzytkownika_id=id_uzytkownika)
            review.save()
            return redirect(f'/info/{film_id}/')

        user = request.user  # Pobieramy użytkownika z requestu
        return render(request, 'movie_info.html', {'film': film, 'opinie': opinie, 'uzytkownicy': uzytkownicy, 'user': user})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = Uzytkownicy.objects.get(E_mail=email)
        except Uzytkownicy.DoesNotExist:
            user = None
        if user is not None and user.check_password(password):
            request.session['user_id'] = user.id
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Nieprawidłowe dane logowania'})
    else:
        return render(request, 'login.html')


def register_view(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password_2 = request.POST['password_2']
        if not email or not username or not password or not password_2:
            return render(request, 'register.html', {'error': 'Wszystkie pola są wymagane.'})

        if Uzytkownicy.objects.filter(E_mail=email).exists():
            return render(request, 'register.html', {'error': 'Konto o podanym adresie e-mail już istnieje.'})

        if Uzytkownicy.objects.filter(Nazwa_Uzytkownika=username).exists():
            return render(request, 'register.html', {'error': 'Konto o podanej nazwie użytkownika już istnieje.'})

        if password != password_2:
            return render(request, 'register.html', {'error': 'Hasła nie są identyczne.'})

        uzytkownicy = Uzytkownicy.objects.create(Nazwa_Uzytkownika=username, E_mail=email, Publiczne=False)
        uzytkownicy.set_password(password)
        uzytkownicy.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')


def logged_user_account_view(request):
    if request.method == 'POST':
        if request.POST.get('formType') == 'data':
            Nazwa_Uzytkownika = request.POST['username']
            E_mail = request.POST['email']
            password = request.POST['password']
            id_uzytkownika = request.POST['id_uzytkownika']
            uzytkownik = Uzytkownicy.objects.get(id_uzytkownika=id_uzytkownika)
            if uzytkownik.check_password(password):
                uzytkownik.Nazwa_Uzytkownika = Nazwa_Uzytkownika
                uzytkownik.E_mail = E_mail
                uzytkownik.save()
                return redirect('/user')
            else:
                return render(request, 'my_account.html', {'error': 'Hasło jest niepoprawne'})
        else:
            oldPassword = request.POST.get('oldPassword')
            id_uzytkownika = request.POST.get('id_uzytkownika')
            uzytkownik = Uzytkownicy.objects.get(id=id_uzytkownika)
            if uzytkownik.check_password(oldPassword):
                newPassword = request.POST.get('newPassword')
                confirmPassword = request.POST.get('confirmPassword')
                if newPassword == confirmPassword:
                    uzytkownik.set_password(newPassword)
                else:
                    return render(request, 'my_account.html', {'error': 'Hasła nie są identyczne.'})
            else:
                return render(request, 'my_account.html', {'error': 'Stare hasło nie jest poprawne'})

    user = request.user  # Pobieramy użytkownika z requestu

    if user.id is not None:
        return render(request, 'my_account.html', {'user': user})
    else:
        return redirect('/login')


def user_account_view(request, user_id):
    try:
        user = get_object_or_404(Uzytkownicy, id=user_id)
    except Http404:
        return render(request, 'missing_data.html', {'data': "użytkownik"})
    else:
        return render(request, 'user_account.html', {'user': user})


def logout_view(request):
    logout(request)
    return redirect('home')


def add_to_watchlist(request, film_id):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user = get_object_or_404(Uzytkownicy, id=user_id)
        film = get_object_or_404(Produkcje, id=film_id)

        Do_obejrzenia.objects.create(ID_Produkcji=film, ID_Uzytkownika=user)
        return redirect('movie_info', film_id=film.id)


def add_to_watchedlist(request, film_id):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user = get_object_or_404(Uzytkownicy, id=user_id)
        film = get_object_or_404(Produkcje, id=film_id)

        Obejrzane.objects.create(ID_Produkcji=film, ID_Uzytkownika=user)
        return redirect('movie_info', film_id=film.id)


def watchlist_view(request, wl_user_id):
    try:
        wl_user = get_object_or_404(Uzytkownicy, id=wl_user_id)
    except Http404:
        return render(request, 'missing_data.html', {'data': "użytkownik"})
    else:
        if not wl_user.Publiczne:
            return render(request, 'watchlist.html',
                          {"error": "Dane tego użytkownika są prywatne, nie można wyświetlić listy."})

        queryset = Do_obejrzenia.objects.filter(ID_Uzytkownika_id=wl_user_id)
        movies_id_list = queryset.values_list('ID_Produkcji_id', flat=True)
        movies = Produkcje.objects.filter(id__in=movies_id_list)

        return render(request, 'watchlist.html', {"items": movies, "wl_user": wl_user, "type": "do obejrzenia"})


def watched_list_view(request, wl_user_id):
    try:
        wl_user = get_object_or_404(Uzytkownicy, id=wl_user_id)
    except Http404:
        return render(request, 'missing_data.html', {'data': "użytkownik"})
    else:
        if not wl_user.Publiczne:
            return render(request, 'watchlist.html',
                          {"error": "Dane tego użytkownika są prywatne, nie można wyświetlić listy."})

        queryset = Obejrzane.objects.filter(ID_Uzytkownika_id=wl_user_id)
        movies_id_list = queryset.values_list('ID_Produkcji_id', flat=True)
        movies = Produkcje.objects.filter(id__in=movies_id_list)

        return render(request, 'watchlist.html', {"items": movies, "wl_user": wl_user, "type": "obejrzanych"})


def my_watchlist_view(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        movie_id = request.POST['movie_id']
        Do_obejrzenia.objects.filter(ID_Uzytkownika_id=user_id, ID_Produkcji_id=movie_id).delete()
        return redirect('my_watchlist_view')

    user_id = request.user.id
    queryset = Do_obejrzenia.objects.filter(ID_Uzytkownika__id=user_id)
    movies_id_list = queryset.values_list('ID_Produkcji_id', flat=True)
    movies = Produkcje.objects.filter(id__in=movies_id_list)

    return render(request, 'my_watchlist.html', {"items": movies, "type": "do obejrzenia"})


def my_watched_list_view(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        movie_id = request.POST['movie_id']
        Obejrzane.objects.filter(ID_Uzytkownika_id=user_id, ID_Produkcji_id=movie_id).delete()
        return redirect('my_watched_list_view')

    user_id = request.user.id
    queryset = Obejrzane.objects.filter(ID_Uzytkownika__id=user_id)
    movies_id_list = queryset.values_list('ID_Produkcji_id', flat=True)
    movies = Produkcje.objects.filter(id__in=movies_id_list)

    return render(request, 'my_watchlist.html', {"items": movies, "type": "obejrzanych"})


class BaseView(generic.base.TemplateView):
    template_name = "base.html"
