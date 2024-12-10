from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.
class UserViewList(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  #Si quiero usar la autenticacion basica
  #authentication_classes = [BasicAuthentication, SessionAuthentication]

  #Si quiero usar tokens
  #authentication_classes = [TokenAuthentication]

  #Si quiero usar tokens
  authentication_classes = [JWTAuthentication]

  permission_classes = [IsAuthenticated]

class LoginView(APIView):
  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user:
      refresh = RefreshToken.for_user(user)
      context = {
        'status': True,
        'content': {
          'username': user.username,
          'email': user.email,
          'token':str(refresh.access_token)
          }
      }
    else:
      context = {
        'status': False,
        'content': 'Credenciales no validas'
      }

    return Response(context)

    # if user is not None:
    #   refresh = RefreshToken.for_user(user)
    #   return Response({
    #     "refresh": str(refresh),
    #     "access": str(refresh.access_token),
    #   })
    # else:
    #   return Response({"error": "Invalid credentials"}, status=401)