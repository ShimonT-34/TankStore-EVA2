from django.db import models

# Create your models here.
class Tanque(models.Model):
    nombre_tanque = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=50)
    imagen = models.URLField(max_length=200)
    
    def __str__(self):
        return self.nombre_tanque
    
    def Total_Bodega(self):
        return self.stock