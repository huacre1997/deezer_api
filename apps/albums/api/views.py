from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.albums.models import Genre
from apps.albums.models import Album
from .serializers import AlbumSerializer, GenreSerializer
from utils.base.viewsets import BaseViewSet
from rest_framework.decorators import action


class GenreViewSet(BaseViewSet):
    """
       retrieve:
       Busca un género por su pk

       list:
       Lista las canciones con estado is_active=True 

       create:
       Crea un género

       update:
       Actualiza un género

    """

    # Obtenemos los datos que queremos devolver.
    queryset = Genre.objects.all()

    # Le indicamos el serializer que debe utilizar para convertir los objetos a JSON.
    serializer_class = GenreSerializer

    # Configuración para que el VIEW sea utilizado por usuarios autenticados.
    permission_classes = [IsAuthenticated]

    # Campos para busqueda
    search_fields = ['name']

    # Campos para ordenar response
    ordering_fields = ['id']

    # Métodos que genera el Viewset
    http_method_names = ["get", "post", "put"]


class AlbumViewSet(BaseViewSet):
    """
       retrieve:
       Busca un album por su pk

       list:
       Lista los albums con estado is_active=True 

       create:
       Crea un album

       update:
       Actualiza un album

    """
    # Obtenemos los datos que queremos devolver.
    queryset = Album.objects.all()

    # Le indicamos el serializer que debe utilizar para convertir los objetos a JSON.
    serializer_class = AlbumSerializer

    # Configuración para que el VIEW sea utilizado por usuarios autenticados.
    permission_classes = [IsAuthenticated]

    # Campos para busqueda
    search_fields = ['title']

    # Campos para ordenar response
    ordering_fields = ['id']

    # Métodos que genera el Viewset
    http_method_names = ["get", "post", "put"]
