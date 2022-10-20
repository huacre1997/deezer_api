from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import UserSerializer


class Register(APIView):
    # Permite el acceso al API sin estar autenticado
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        # Obtenemos los datos
        username = request.data.get("username", "")
        password = request.data.get("password", "")

        # Authenticate verifica las credenciales
        user = authenticate(username=username, password=password)
        if user:
            # update_last_login -> Actualiza la última fecha de login de user
            update_last_login(None, user)
            
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                # Invocamos el UserSerializer para adjuntar los datos del usuario a nuestro Response
                user_serializer = UserSerializer(user)

                return Response({
                    "token": login_serializer.validated_data.get("access"),
                    "refresh-token": login_serializer.validated_data.get("refresh"),
                    "user": user_serializer.data,
                    "message": "Inicio de Sesión Exitoso"
                }, status=status.HTTP_200_OK)
        return Response({'error': 'Usuario o contraseña incorrectos'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh-token"]
            # Creamos un objeto Refresh Token para usar sus métodos
            token = RefreshToken(refresh_token)

            # Envía el refresh token a la tabla Black List donde no volverá a ser válido o utilizado
            token.blacklist()

            return Response({'message': 'Se ha cerrado la sesión'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
