from django.db import models
import uuid

# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id')
    nombre = models.CharField(max_length=250, null=True)
    apellido = models.CharField(max_length=250, null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=250, null=True)

    #Relationship
    

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id')
    nombre = models.CharField(max_length=250, null=True,)
    
    def __str__(self):
        return self.nombre


class Registro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id')
    monto = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    descripcion = models.CharField(max_length=1000, null=True)
    fecha = models.CharField(max_length=250, null=True)

    #Relationship
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE, null=True, blank=True)
