from utils.constants import EXCLUDED_FIELDS
from rest_framework import serializers
from apps.albums.models import Genre, Album


class GenreSerializer(serializers.ModelSerializer):
    picture = serializers.URLField(required=True)
    name = serializers.CharField(required=True)
    """
    Clase para convertir un objeto Genre a un formato JSON.
    """
    class Meta:
        model = Genre
        exclude = [] + EXCLUDED_FIELDS


class AlbumSerializer(serializers.ModelSerializer):
    """
    Clase para convertir un objeto Genre a un formato JSON.
    """
    class Meta:
        model = Album
        exclude = [] + EXCLUDED_FIELDS
