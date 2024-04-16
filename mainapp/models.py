from django.db import models


class Produkcje(models.Model):
    Tytul = models.CharField(max_length=50)
    Rezyser = models.CharField(max_length=50)
    Dlugosc_ilosc_odcinkow = models.IntegerField()
    Opis = models.CharField(max_length=1000)
    Data_premiery = models.DateField()

    def __str__(self):
        return self.Tytul

class Do_obejrzenia(models.Model):
    ID_Produkcji = models.ForeignKey(Produkcje, on_delete=models.CASCADE)
    ID_Uzytkownika = models.ForeignKey(Uzytkownicy, on_delete=models.CASCADE)

class Rezencje(models.Model):
    Ocena = models.IntegerField()
    Komentarz = models.TextField()
    ID_Uzytkownika = models.ForeignKey()
    ID_Produkcji = models.ForeignKey()

    def __str__(self):
        return self.Komentarz


class Uzytkownicy(models.Model):
    Nazwa_Uzytkownika = models.TextField()
    Haslo = models.TextField()
    E_mail = models.TextField()
    Publiczne = models.BooleanField()

    def __str__(self):
        return self.Nazwa_Uzytkownika

class Obejrzane(models.Model):
    ID_Produkcji = models.ForeignKey(Produkcje, on_delete=models.CASCADE)
    ID_Uzytkownika = models.ForeignKey(Uzytkownicy, on_delete=models.CASCADE)
