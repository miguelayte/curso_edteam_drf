from django.urls import path
from . import views
urlpatterns = [
  path('categorias/', views.CategoriaList.as_view()),
  path('productos/', views.ProductoList.as_view()),
  path('clientes/', views.ClienteList.as_view()),
  path('categorias/<int:pk>', views.CategoriaDetail.as_view()),
  path('productos/<int:pk>', views.ProductoDetail.as_view()),
  path('clientes/<int:pk>', views.ClienteDetail.as_view()),
  path('categorias/<int:categoria_id>/productos', views.CategoriaProductosView.as_view()),
  path('pedidos/', views.PedidoCreateView.as_view()),
]
