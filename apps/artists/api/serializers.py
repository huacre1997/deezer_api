from rest_framework import serializers
from apps.artists.models import Artist
from utils.constants import EXCLUDED_FIELDS


class ArtistSerializer(serializers.ModelSerializer):
    """
    Clase para convertir un objeto Genre a un formato JSON.
    """
    class Meta:
        model = Artist
        exclude = [] + EXCLUDED_FIELDS