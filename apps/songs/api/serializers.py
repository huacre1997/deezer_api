from rest_framework.serializers import ModelSerializer
from apps.songs.models import Song
from utils.constants import EXCLUDED_FIELDS


class SongSerializer(ModelSerializer):
    """
    Clase para convertir un objeto Song a un formato JSON.
    """
    class Meta:
        model = Song
        exclude = [] + EXCLUDED_FIELDS
