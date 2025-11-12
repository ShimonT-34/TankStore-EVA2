from django.contrib import admin
from . models import Tanque, Categoria

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    listdisplay = ["nombre_tanque", "precio", "stock", "descripcion", "imagen", "pais", "categoria"]

admin.site.register(Tanque)
admin.site.register(Categoria, CategoriaAdmin)