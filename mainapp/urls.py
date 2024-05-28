from django.contrib import admin
from django.urls import path
from mainapp import views
from .views import widok_home, details_view, login_view, register_view, logged_user_account_view, user_account_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", widok_home, name="home"),
    path("info/<int:film_id>/", details_view, name="movie_info"),
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('user/', logged_user_account_view, name="user"),
    path('user/<int:user_id>/', user_account_view, name="user"),
    path('RSWTA/', views.BaseView.as_view(), name='RSWTA'),  # imo już można wyjebać, bo mamy podpięty base do reszty
    path('logout/', views.logout_view, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)