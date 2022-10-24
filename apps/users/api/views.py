from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework import status

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import RegisterSerializer, LogoutSerializer


class Register(GenericAPIView):
    """
    Registra nuevos usuarios
    """
    # Permite el acceso al API sin estar autenticado
    permission_classes = [AllowAny]

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Guarda el usuario
            serializer.save()

            # Enviamos las credenciales al serializer del login
            login_serializer = TokenObtainPairSerializer(
                data=serializer._validated_data)
            if login_serializer.is_valid():
                token = login_serializer.validated_data.get("access")
                refresh_token = login_serializer.validated_data.get("refresh")
            return Response({
                'token': token,
                'refresh_token': refresh_token,
                "user": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(TokenObtainPairView):
    """
    Login del user
    """
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data)
        if login_serializer.is_valid():
            token = login_serializer.validated_data.get("access")
            refresh_token = login_serializer.validated_data.get("refresh")
            return Response({
                "token": token,
                "refresh_token": refresh_token
            }, status=status.HTTP_200_OK)
        return Response({
            'error': 'Username or password are incorrect'
        }, status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    """
    Logout
    """
    serializer_class = LogoutSerializer

    # Bloquear el acceso al API sin estar autenticado
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'message': 'Successful logout'
            }, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
