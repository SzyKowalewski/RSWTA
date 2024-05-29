from django.contrib import admin

from .models import Produkcje

from .models import Uzytkownicy

from .models import Do_obejrzenia

admin.site.register(Do_obejrzenia)

from .models import Rezencje

admin.site.register(Rezencje)

from .models import Obejrzane

admin.site.register(Obejrzane)

from .models import Kategorie

admin.site.register(Kategorie)

'''
class ChoiceInline(admin.TabularInline):
    model = Do_obejrzenia
    extra = 1
    '''
class ProdukcjeAdmin(admin.ModelAdmin):
    list_display = ["Tytul", "Rezyser", "ID_Kategorii"]

    fieldsets = [
        (None, {
            "fields": ["Tytul", "Rezyser",]
        }),
        ("Informacje dodatkowe", {
            "fields": ["Opis","Dlugosc_ilosc_odcinkow", "ID_Kategorii","Data_premiery"],
            "classes": ["collapse"]
        }),
    ]
    #inlines = [ChoiceInline]
    list_filter = ["Rezyser", "ID_Kategorii"]
    search_fields = ["Tytul", "Rezyser"]

class UzytkownicyAdmin(admin.ModelAdmin):
    list_display = ["Nazwa_Uzytkownika", "E_mail"]
    search_fields = ["Nazwa_Uzytkownika", "E_mail"]

    fields =["Nazwa_Uzytkownika", "E_mail","Publiczne"]

admin.site.register(Produkcje, ProdukcjeAdmin)

admin.site.register(Uzytkownicy, UzytkownicyAdmin)