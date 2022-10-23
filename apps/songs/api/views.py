from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.songs.models import Song
from .serializers import SongSerializer
from utils.base.viewsets import BaseViewSet
from rest_framework.decorators import action


class SongViewSet(BaseViewSet):
    """
    Clase ViewSet de Genre
    """

    # Obtenemos los datos que queremos devolver.
    queryset = Song.objects.all()

    # Le indicamos el serializer que debe utilizar para convertir los objetos a JSON.
    serializer_class = SongSerializer

    # Configuración para que el VIEW sea utilizado por usuarios autenticados.
    permission_classes = [IsAuthenticated]

    search_fields = ['title']

    ordering_fields = ['id', 'title']

    http_method_names = ["get", "post", "put"]
