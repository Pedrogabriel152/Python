from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    foto = get_object_or_404(Fotografia, pk=foto_id);
    return render(request, 'galeria/imagem.html', {"foto": foto})

def buscar(request):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    
    if "buscar" in request.GET:
        nome = request.GET['buscar']
        if nome:
            fotografias = fotografias.filter(nome__icontains=nome)
    return render(request, 'galeria/buscar.html', {"cards": fotografias});