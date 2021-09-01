from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, Http404, get_object_or_404, redirect
from .models import Game, Empresa
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    dados = Game.objects.order_by('id').filter(
        mostrar=True
    )
    return render(request, 'home/index.html', {'dados': dados})

def empresa(request):
    dados = Empresa.objects.order_by('id')
    return render(request, 'home/empresas.html', {'dados': dados})

def sobre(request):
    return render(request, 'home/sobre.html')

def mostrarGame(request, idBusca):
    dados = get_object_or_404(Game, id=idBusca)
    return render(request, 'home/detGame.html', {'dados':dados})


def buscar(request):
    x = request.GET['buscar']

    if x is None or not x:
        messages.add_message(request, messages.INFO, 'Como o nada foi digitado, todos os games estão sendo mostrados!')
        redirect('home')
    else:
        messages.add_message(request, messages.SUCCESS, 'Busca com sucesso!')
    dados = Game.objects.order_by('id').filter(
        Q(nome__icontains=x) | Q(descricao__icontains=x)
    )

    return render(request, 'home/index.html', {'dados': dados})
