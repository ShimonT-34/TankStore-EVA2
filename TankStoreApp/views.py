from django.shortcuts import render
# Importando modelos a usar
from . models import Tanque

# Create your views here.
def pagina_principal(request):
    return render(request, "pagina_principal.html")

def pagina_categoria(request):
    return render(request, "pagina_categoria.html")

def pagina_detalle(request):
    return render(request, "pagina_detalle.html")