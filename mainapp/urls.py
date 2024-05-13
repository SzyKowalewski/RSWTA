from django.contrib import admin
from django.urls import path
from mainapp import views
from .views import widok_home, details_view

urlpatterns = [
    path("", widok_home, name="home"),
    path("info/", details_view, name="movie_info"),
    path('admin/', admin.site.urls),
    path('RSWTA/', views.BaseView.as_view(), name='RSWTA')  # imo już można wyjebać, bo mamy podpięty base do reszty
]