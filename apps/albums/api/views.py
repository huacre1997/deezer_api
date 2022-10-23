from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.albums.models import Genre
from apps.albums.models import Album
from .serializers import GenreSerializer
from utils.base.viewsets import BaseViewSet
from rest_framework.decorators import action


class GenreViewSet(BaseViewSet):
    """
    Clase ViewSet de Genre
    """

    # Obtenemos los datos que queremos devolver.
    queryset = Genre.objects.all()

    # Le indicamos el serializer que debe utilizar para convertir los objetos a JSON.
    serializer_class = GenreSerializer

    # Configuración para que el VIEW sea utilizado por usuarios autenticados.
    permission_classes = [IsAuthenticated]

    search_fields = ['name']

    ordering_fields = ['id', 'name']

    http_method_names = ["get", "post", "put"]


class AlbumViewSet(BaseViewSet):
    """
    Clase ViewSet de Genre
    """

    # Obtenemos los datos que queremos devolver.
    queryset = Album.objects.all()

    # Le indicamos el serializer que debe utilizar para convertir los objetos a JSON.
    serializer_class = GenreSerializer

    # Configuración para que el VIEW sea utilizado por usuarios autenticados.
    permission_classes = [IsAuthenticated]

    search_fields = ['name']

    ordering_fields = ['id', 'name']

    http_method_names = ["get", "post", "put"]
