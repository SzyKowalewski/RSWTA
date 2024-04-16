from django.contrib import admin

from .models import Produkcje

admin.site.register(Produkcje)

from .models import Uzytkownicy

admin.site.register(Uzytkownicy)

from .models import Do_obejrzenia

admin.site.register(Do_obejrzenia)

from .models import Rezencje

admin.site.register(Rezencje)

from .models import Obejrzane

admin.site.register(Obejrzane)