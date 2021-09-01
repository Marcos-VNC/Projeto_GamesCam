from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='home_login'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='cadastrar'),
    path('logout/', views.logout, name='logout')
]
