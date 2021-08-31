from django.db.models import Q
from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.contrib import messages
from .models import Game


# Create your views here.
def index(request):
    dados = Game.objects.order_by('id').filter(
        mostrar=True
    )
    return render(request, 'home/index.html', {'dados': dados})