from django.db import models


class Produkcje(models.Model): # NOQA
    Tytul = models.CharField(max_length=50) # NOQA
    Rezyser = models.CharField(max_length=50) # NOQA
    Dlugosc_ilosc_odcinkow = models.IntegerField() # NOQA
    Opis = models.CharField(max_length=1000) # NOQA
    Data_premiery = models.DateField() # NOQA

    def __str__(self):
        return self.Tytul


class Uzytkownicy(models.Model): # NOQA
    Nazwa_Uzytkownika = models.TextField() # NOQA
    Haslo = models.TextField() # NOQA
    E_mail = models.TextField()
    Publiczne = models.BooleanField() # NOQA

    def __str__(self):
        return self.Nazwa_Uzytkownika


class Do_obejrzenia(models.Model): # NOQA
    ID_Produkcji = models.ForeignKey(Produkcje, on_delete=models.CASCADE) # NOQA
    ID_Uzytkownika = models.ForeignKey(Uzytkownicy, on_delete=models.CASCADE) # NOQA


class Rezencje(models.Model): # NOQA
    Ocena = models.IntegerField() # NOQA
    Komentarz = models.TextField() # NOQA
    ID_Uzytkownika = models.ForeignKey(Uzytkownicy, on_delete=models.CASCADE) # NOQA
    ID_Produkcji = models.ForeignKey(Produkcje, on_delete=models.CASCADE) # NOQA

    def __str__(self):
        return self.Komentarz


class Obejrzane(models.Model): # NOQA
    ID_Produkcji = models.ForeignKey(Produkcje, on_delete=models.CASCADE) # NOQA
    ID_Uzytkownika = models.ForeignKey(Uzytkownicy, on_delete=models.CASCADE) # NOQA
