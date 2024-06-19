from django.contrib import admin
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Kategorie(models.Model):
    """
    Model representing a category.

    Attributes:
        Nazwa (TextField): The name of the category.
    """

    class Meta:
        verbose_name_plural = 'Kategorie'

    Nazwa = models.TextField()

    def __str__(self):
        """
        Returns the string representation of the category.

        Returns:
            str: The name of the category.
        """
        return self.Nazwa


class Produkcje(models.Model):
    """
    Model representing a production (film or series).

    Attributes:
        Tytul (CharField): The title of the production.
        Rezyser (CharField): The director of the production.
        Dlugosc_ilosc_odcinkow (IntegerField): The length or number of episodes.
        Opis (CharField): The description of the production.
        Data_premiery (DateField): The release date of the production.
        ID_Kategorii (ForeignKey): The category of the production.
        Plakat (ImageField): The poster image of the production.
    """

    class Meta:
        verbose_name_plural = 'Produkcje'

    Tytul = models.CharField(max_length=50)
    Rezyser = models.CharField(max_length=50)
    Dlugosc_ilosc_odcinkow = models.IntegerField()
    Opis = models.CharField(max_length=1000)
    Data_premiery = models.DateField()
    ID_Kategorii = models.ForeignKey(Kategorie, verbose_name="Kategoria", on_delete=models.CASCADE)
    Plakat = models.ImageField(upload_to='plakaty/', null=True, blank=True)

    def __str__(self):
        """
        Returns the string representation of the production.

        Returns:
            str: The title of the production.
        """
        return self.Tytul

    def average_rating(self):
        """
        Calculates the average rating of the production.

        Returns:
            float: The average rating of the production.
        """
        opinie = self.rezencje_set.all()
        if not opinie:
            return 0
        total_score = sum(opinia.Ocena for opinia in opinie)
        return total_score / len(opinie)


class Uzytkownicy(models.Model):
    """
    Model representing a user.

    Attributes:
        Nazwa_Uzytkownika (TextField): The username of the user.
        Haslo (CharField): The hashed password of the user.
        E_mail (TextField): The email address of the user.
        Publiczne (BooleanField): Whether the user's profile is public.
    """

    class Meta:
        verbose_name_plural = 'Uzytkownicy'

    Nazwa_Uzytkownika = models.TextField()
    Haslo = models.CharField(max_length=128)
    E_mail = models.TextField()
    Publiczne = models.BooleanField()

    def __str__(self):
        """
        Returns the string representation of the user.

        Returns:
            str: The username of the user.
        """
        return self.Nazwa_Uzytkownika

    def set_password(self, raw_password):
        """
        Sets the user's password.

        Args:
            raw_password (str): The raw password to set.
        """
        self.Haslo = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        """
        Checks the user's password.

        Args:
            raw_password (str): The raw password to check.

        Returns:
            bool: True if the password is correct, False otherwise.
        """
        return check_password(raw_password, self.Haslo)


class Do_obejrzenia(models.Model):
    """
    Model representing a watchlist entry.

    Attributes:
        ID_Produkcji (ForeignKey): The production to watch.
        ID_Uzytkownika (ForeignKey): The user who wants to watch the production.
    """

    class Meta:
        verbose_name_plural = 'Do_obejrzenia'

    ID_Produkcji = models.ForeignKey(Produkcje, verbose_name="Nazwa Produkcji", on_delete=models.CASCADE)
    ID_Uzytkownika = models.ForeignKey(Uzytkownicy, verbose_name="Nazwa Użytkownika", on_delete=models.CASCADE)


class Rezencje(models.Model):
    """
    Model representing a review.

    Attributes:
        Ocena (IntegerField): The rating of the production.
        Komentarz (TextField): The comment about the production.
        ID_Uzytkownika (ForeignKey): The user who wrote the review.
        ID_Produkcji (ForeignKey): The production being reviewed.
    """

    class Meta:
        verbose_name_plural = 'Rezencje'
        unique_together = ('ID_Uzytkownika', 'ID_Produkcji')

    Ocena = models.IntegerField()
    Komentarz = models.TextField()
    ID_Uzytkownika = models.ForeignKey(Uzytkownicy, verbose_name="Nazwa Użytkownika", on_delete=models.CASCADE)
    ID_Produkcji = models.ForeignKey(Produkcje, verbose_name="Nazwa Produkcji", on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns the string representation of the review.

        Returns:
            str: The comment of the review.
        """
        return self.Komentarz


class Obejrzane(models.Model):
    """
    Model representing a watched list entry.

    Attributes:
        ID_Produkcji (ForeignKey): The production that was watched.
        ID_Uzytkownika (ForeignKey): The user who watched the production.
    """

    class Meta:
        verbose_name_plural = 'Obejrzane'

    ID_Produkcji = models.ForeignKey(Produkcje, verbose_name="Nazwa Produkcji", on_delete=models.CASCADE)
    ID_Uzytkownika = models.ForeignKey(Uzytkownicy, verbose_name="Nazwa Użytkownika", on_delete=models.CASCADE)
