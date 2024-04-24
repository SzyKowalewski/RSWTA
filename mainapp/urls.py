from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("RSWTA/", include("urls.py")),
    path("admin/", admin.site.urls),
]