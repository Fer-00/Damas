from django.urls import path

from . import views

urlpatterns = [
    path('', views.partida),
    path('/jogada', views.jogada)
]
