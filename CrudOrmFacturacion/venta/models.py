from django.db import models

class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField(default=0)
    stock = models.FloatField(default=0)
    iva = models.BooleanField(default=True)


class Cliente(models.Model):
    ruc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=300)
    direccion = models.TextField(blank= True,null=True)
    producto = models.ManyToManyField(Producto)

class Factura(models.Model):
    cliente= models.ForeignKey(Cliente,on_delete=models.CASCADE)
    fecha = models.DateField()
    total = models.FloatField(default=0)

class DetalleFactura(models.Model):
    factura= models.ForeignKey(Factura,on_delete=models.CASCADE)
    producto= models.ForeignKey(Producto,on_delete=models.CASCADE)

