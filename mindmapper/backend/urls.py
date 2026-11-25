from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.redirect_home),
    path("home", views.index), 
    path("load", views.load), 
    path("how-it-works", views.how_it_works)
]