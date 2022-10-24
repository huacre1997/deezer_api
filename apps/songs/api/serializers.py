from rest_framework import serializers
from apps.songs.models import Song
from utils.constants import EXCLUDED_FIELDS
from apps.artists.api.serializers import ArtistSerializer
from apps.albums.api.serializers import AlbumSerializer


class SongSerializer(serializers.ModelSerializer):
    """
    Clase para convertir un objeto Song a un formato JSON.
    """

    class Meta:
        model = Song
        exclude = [] + EXCLUDED_FIELDS

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["artist"] = ArtistSerializer(instance.artist).data
        data["album"] = AlbumSerializer(instance.album).data
        return data
