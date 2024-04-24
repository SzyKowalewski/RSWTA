from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path('admin/', admin.site.urls),
]