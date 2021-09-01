from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('empresa/', views.empresa, name='empresa'),
    path('<int:idBusca>', views.mostrarGame, name='game'),
    path('buscar/', views.buscar, name='buscar'),
]
