from django.urls import path
from . import views

urlpatterns = [
  path('usuario', views.UserViewList.as_view()),
  #path('usuario/<int:pk>', views.UserDetail.as_view()),
  path('login', views.LoginView.as_view()),
]