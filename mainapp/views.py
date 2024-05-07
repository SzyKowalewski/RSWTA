from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import generic
from .models import Produkcje

class HomeView(generic.base.TemplateView):
   template_name = "home.html"
def widok_home(request):
    filmy = Produkcje.objects.all()
    return render(request, 'home.html', {'filmy': filmy})

class BaseView(generic.base.TemplateView):
    template_name = "base.html"
