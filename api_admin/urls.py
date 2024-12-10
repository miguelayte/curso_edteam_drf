from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views

router = DefaultRouter()
router.register('categorias', views.CategoriaViewSet, basename='categorias')
router.register('productos', views.ProductoViewSet, basename='productos')

urlpatterns=router.urls
