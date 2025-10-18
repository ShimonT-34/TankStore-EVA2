from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Tanque(models.Model):
    nombre_tanque = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=100)
    imagen = models.URLField(max_length=200)
    pais = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_tanque + "----" + self.pais + " ------ " + f"{self.stock}" + " ----- " + f"{self.precio}" + " ---- " + self.descripcion