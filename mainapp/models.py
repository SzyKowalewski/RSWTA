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

