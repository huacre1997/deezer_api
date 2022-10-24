from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
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
    permission_classes = [permissions.IsAuthenticated]

    search_fields = ['title']

    ordering_fields = ['id', 'title']

    http_method_names = ["get", "post", "put"]

    @action(detail=False, methods=['get'], name='Buscar canción')
    def search(self, request, pk=None):
        """
        Método que busca una canción a traves del param "p"
        """
        q = self.request.query_params.get('q')
        qs = self.get_queryset()
        if q:
            # Filtra por título , título corto o nombre de artista
            qs = qs.filter(
                Q(title__icontains=q) | Q(title_short__icontains=q) | Q(
                    artist__name__icontains=q)
            )
        serializer = self.get_serializer(qs, many=True)

        return Response(serializer.data)
