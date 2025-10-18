from django.shortcuts import render, get_object_or_404
# Importando modelos a usar
from . models import Tanque, Categoria

# Create your views here.
def pagina_principal(request):
    tanques = Tanque.objects.all()
    categorias = Categoria.objects.all()

    context = {
        'tanques': tanques,
        'categorias': categorias,
        'titulo': 'TANKSTORE - Principal'
    }
    return render(request, "pagina_principal.html", context)

def pagina_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    tanques = Tanque.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()

    context = {
        'tanques': tanques,
        'categorias': categorias,
        'categoria_actual': categoria,
        'titulo': f'TANKSTORE - {categoria.nombre}'
    }
    return render(request, "pagina_categoria.html", context)

def pagina_detalle(request, tanque_id):
    tanque = get_object_or_404(Tanque, id=tanque_id)

    context = {
        'tanque': tanque,
        'titulo': f'TANKSTORE - {tanque.nombre_tanque}'
    }
    return render(request, "pagina_detalle.html", context)




