from rest_framework.serializers import ModelSerializer
from apps.songs.models import Song


class SongSerializer(ModelSerializer):
    """
    Clase para convertir un objeto Song a un formato JSON.
    """
    class Meta:
        model = Song
        fields = '__all__'
