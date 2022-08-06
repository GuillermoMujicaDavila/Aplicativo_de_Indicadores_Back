from pickle import TRUE
from pyexpat import model
from django.db import models

class Usuario(models.Model):
    idUser = models.AutoField(primary_key=True)
    rucDni = models.CharField( max_length=45,null=False)
    nombreUser = models.CharField(max_length=500,null=False)
    apellidoUser = models.CharField(max_length= 500,null=False)
    edadUser = models.IntegerField(null=False)
    generoUser = models.BooleanField(default=TRUE)
    correoUser = models.EmailField(max_length=500)
    passwordUser = models.
    
    
    

class Vendedor(models.Model):
    pass


# Create your models here.
