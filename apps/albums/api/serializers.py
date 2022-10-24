from utils.constants import EXCLUDED_FIELDS
from rest_framework import serializers
from apps.albums.models import Genre, Album
from apps.artists.api.serializers import ArtistSerializer


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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["artist"] = ArtistSerializer(instance.artist).data
        data["genre"] = GenreSerializer(instance.genre).data
        return data
