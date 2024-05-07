from django.contrib import admin
from django.urls import path
from mainapp import views
from .views import widok_home

urlpatterns = [
    path("", widok_home, name="home"),
    path('admin/', admin.site.urls),
    path('RSWTA/', views.BaseView.as_view(), name='RSWTA')
]