from rest_framework import generics
from .models import Producto, Categoria, Cliente, Pedido
from .serializers import ProductoSerializer, CategoriaSerializer, ClienteSerializer, CategoriaProductoSerializer, PedidoSerializer

# Create your views here.
class CategoriaList(generics.ListCreateAPIView):
  queryset = Categoria.objects.all()
  serializer_class = CategoriaSerializer

class ProductoList(generics.ListCreateAPIView):
  queryset = Producto.objects.all()
  serializer_class = ProductoSerializer

class ClienteList(generics.ListCreateAPIView):
  queryset = Cliente.objects.all()
  serializer_class = ClienteSerializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Producto.objects.all()
  serializer_class = ProductoSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Categoria.objects.all()
  serializer_class = CategoriaSerializer

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Cliente.objects.all()
  lookup_url_kwarg = 'pk'
  serializer_class = ClienteSerializer

class CategoriaProductosView(generics.RetrieveAPIView):
  queryset = Categoria.objects.all()
  lookup_url_kwarg = 'categoria_id'
  serializer_class = CategoriaProductoSerializer

class PedidoCreateView(generics.CreateAPIView):
  queryset = Pedido.objects.all()
  serializer_class = PedidoSerializer