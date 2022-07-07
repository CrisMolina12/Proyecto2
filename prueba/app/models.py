from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=51)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=True, blank=True)
    imagen = models.ImageField(upload_to="productos/", null=True)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

class Publicar(models.Model):
        nombre = models.CharField(max_length=51)
        descripcion = models.CharField(max_length=100)
        precio = models.IntegerField()
        categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
        cantidad = models.IntegerField(null=True, blank=True)
        
        
        def __str__(self):
            return self.nombre