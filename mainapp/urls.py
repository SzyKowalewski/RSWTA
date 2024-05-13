from django.contrib import admin
from django.urls import path
from mainapp import views
from .views import widok_home, details_view, login_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", widok_home, name="home"),
    path("info/", details_view, name="movie_info"),
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('RSWTA/', views.BaseView.as_view(), name='RSWTA'),  # imo już można wyjebać, bo mamy podpięty base do reszty
    path('logout/', views.logout_view, name='logout'),
]