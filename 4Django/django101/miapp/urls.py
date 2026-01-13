from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('juegos/<int:id>/', views.detalle_juego, name='detalle_juego')
]