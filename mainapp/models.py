from django.contrib import admin
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Kategorie(models.Model): # NOQA
    class Meta:
        verbose_name_plural = 'Kategorie'
    Nazwa = models.TextField() # NOQA

    def __str__(self):
        return self.Nazwa


class Produkcje(models.Model): # NOQA
    class Meta:
        verbose_name_plural = 'Produkcje'
    Tytul = models.CharField(max_length=50) # NOQA
    Rezyser = models.CharField(max_length=50) # NOQA
    Dlugosc_ilosc_odcinkow = models.IntegerField() # NOQA
    Opis = models.CharField(max_length=1000) # NOQA
    Data_premiery = models.DateField() # NOQA
    ID_Kategorii = models.ForeignKey(Kategorie,verbose_name="Kategoria", on_delete=models.CASCADE) # NOQA
    Plakat = models.ImageField(upload_to='plakaty/', null=True, blank=True)
    def __str__(self):
        return self.Tytul

    def average_rating(self):
        opinie = self.rezencje_set.all()
        if not opinie:
            return 0
        total_score = sum(opinia.Ocena for opinia in opinie)
        return total_score / len(opinie)

class Uzytkownicy(models.Model): # NOQA
    class Meta:
        verbose_name_plural = 'Uzytkownicy'
    Nazwa_Uzytkownika = models.TextField() # NOQA
    Haslo = models.CharField(max_length=128)  # NOQA
    E_mail = models.TextField()
    Publiczne = models.BooleanField() # NOQA

    def __str__(self):
        return self.Nazwa_Uzytkownika

    def set_password(self, raw_password):
        self.Haslo = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.Haslo)

class Do_obejrzenia(models.Model): # NOQA
    class Meta:
        verbose_name_plural = 'Do_obejrzenia'
    ID_Produkcji = models.ForeignKey(Produkcje,verbose_name="Nazwa Produkcji", on_delete=models.CASCADE) # NOQA
    ID_Uzytkownika = models.ForeignKey(Uzytkownicy,verbose_name="Nazwa Użytkownika", on_delete=models.CASCADE) # NOQA


class Rezencje(models.Model): # NOQA
    class Meta:
        verbose_name_plural = 'Rezencje'
        unique_together = ('ID_Uzytkownika', 'ID_Produkcji')
    Ocena = models.IntegerField() # NOQA
    Komentarz = models.TextField() # NOQA
    ID_Uzytkownika = models.ForeignKey(Uzytkownicy,verbose_name="Nazwa Użytkownika", on_delete=models.CASCADE) # NOQA
    ID_Produkcji = models.ForeignKey(Produkcje,verbose_name="Nazwa Produkcji", on_delete=models.CASCADE) # NOQA

    def __str__(self):
        return self.Komentarz


class Obejrzane(models.Model): # NOQA
    class Meta:
        verbose_name_plural = 'Obejrzane'
    ID_Produkcji = models.ForeignKey(Produkcje,verbose_name="Nazwa Produkcji", on_delete=models.CASCADE) # NOQA
    ID_Uzytkownika = models.ForeignKey(Uzytkownicy,verbose_name="Nazwa Użytkownika", on_delete=models.CASCADE) # NOQA
