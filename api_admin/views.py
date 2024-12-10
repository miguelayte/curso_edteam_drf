from rest_framework import viewsets
from api.models import Producto, Categoria
from api.serializers import ProductoSerializer, CategoriaSerializer

# Create your views here.
class CategoriaViewSet(viewsets.ModelViewSet):
  queryset = Categoria.objects.all()
  serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
  queryset = Producto.objects.all()
  serializer_class = ProductoSerializer

