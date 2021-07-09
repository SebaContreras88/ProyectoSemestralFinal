from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id')
    nombreCategoria = models.CharField(max_length=50,verbose_name='Categoría')
    def __str__(self):
        return self.nombreCategoria

class Arte(models.Model):
    numarticulo = models.CharField(primary_key=True,max_length=10,null=False,blank=False,verbose_name='Numarticulo')
    nombre = models.CharField(max_length=20,null=False,blank=False,verbose_name='Nombre')
    precio = models.CharField(max_length=20,null=False,blank=False,verbose_name='Precio')
    autor = models.CharField(max_length=20,null=False,blank=False,verbose_name='Autor')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.numarticulo