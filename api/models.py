from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Categoria(models.Model):
  nombre = models.CharField(max_length=100)

  def __str__(self):
    return self.nombre

class Producto(models.Model):
  nombre = models.CharField(max_length=200)
  precio = models.DecimalField(max_digits=10, decimal_places=2)
  imagen = CloudinaryField('image',default='')
  categoria = models.ForeignKey(Categoria, related_name='Productos', on_delete=models.RESTRICT)

  def __str__(self):
    return self.nombre

class Cliente(models.Model):
  nombre = models.CharField(max_length=200)
  email = models.EmailField()
  telefono = models.CharField(max_length=20)
  direccion = models.TextField()

  def __str__(self):
    return f"{self.nombre}"

class Pedido(models.Model):
  codigo = models.CharField(max_length=10, primary_key=True)
  cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
  fecha_pedido = models.DateTimeField(auto_now_add=True)

class PedidoProducto(models.Model):
  pedido = models.ForeignKey(Pedido, related_name='pedido_productos', on_delete=models.RESTRICT)
  producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
  cantidad = models.PositiveIntegerField(default=1)