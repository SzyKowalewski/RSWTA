from django.contrib import admin
from django.urls import path
from mainapp import views
from .views import widok_home, details_view, login_view, register_view, logged_user_account_view, user_account_view, add_to_watchlist, add_to_watchedlist, watchlist_view
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
    path('add_to_watchlist/<int:film_id>/', add_to_watchlist, name='add_to_watchlist'),
    path('add_to_watchedlist/<int:film_id>/', add_to_watchedlist, name='add_to_watchedlist'),
    path('watchlist/<int:wl_user_id>/', watchlist_view, name='watchlist_view'),
    path('watched_list/<int:wl_user_id>/', views.watched_list_view, name='watched_list_view'),
    path('my_watchlist/', views.my_watchlist_view, name='my_watchlist_view'),
    path('my_watched_list/', views.my_watched_list_view, name='my_watched_list_view'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)