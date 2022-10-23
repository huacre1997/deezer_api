from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.artists.models import Artist
from .serializers import ArtistSerializer
from utils.base.viewsets import BaseViewSet
from rest_framework.decorators import action


class ArtistViewSet(BaseViewSet):
    """
    Clase ViewSet de Genre
    """

    # Obtenemos los datos que queremos devolver.
    queryset = Artist.objects.all()

    # Le indicamos el serializer que debe utilizar para convertir los objetos a JSON.
    serializer_class = ArtistSerializer

    # Configuración para que el VIEW sea utilizado por usuarios autenticados.
    permission_classes = [IsAuthenticated]

    search_fields = ['name']

    ordering_fields = ['id', 'name']

    http_method_names = ["get", "post", "put"]
