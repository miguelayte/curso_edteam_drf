from rest_framework import serializers
from .models import Producto, Categoria, Cliente, Pedido, PedidoProducto

class CategoriaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Categoria
    fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Producto
    fields = '__all__'

  def to_representation(self, instance):
    representation = super().to_representation(instance)
    representation['imagen'] = instance.imagen.url
    return representation

class ClienteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cliente
    fields = '__all__'  

""" serializers de tablas relacionadas """
class CategoriaProductoSerializer(serializers.ModelSerializer):
  Productos = ProductoSerializer(many=True, read_only=True)

  class Meta:
    model = Categoria
    fields = ['id', 'nombre', 'Productos']

class PedidoProductoSerializer(serializers.ModelSerializer):
  class Meta:
    model = PedidoProducto
    fields = ['producto', 'cantidad']

class PedidoSerializer(serializers.ModelSerializer):
  pedido_productos = PedidoProductoSerializer(many=True)

  class Meta:
    model = Pedido
    fields = ['codigo', 'cliente', 'pedido_productos']

  def create(self, validated_data):
    pedido_productos_data = validated_data.pop('pedido_productos')
    pedido = Pedido.objects.create(**validated_data)
    for pedido_producto_data in pedido_productos_data:
      PedidoProducto.objects.create(pedido=pedido, **pedido_producto_data)
    return pedido