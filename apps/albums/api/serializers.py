from email.policy import default
from rest_framework.serializers import ModelSerializer
from apps.albums.models import Genre, Album
from rest_framework import serializers
from utils.choices import Type


class GenreSerializer(serializers.ModelSerializer):
    picture = serializers.URLField(required=True)
    name = serializers.CharField(required=True)
    """
    Clase para convertir un objeto Genre a un formato JSON.
    """
    class Meta:
        model = Genre
        fields = ('id', 'name', 'picture', 'type')


class AlbumSerializer(serializers.ModelSerializer):
    """
    Clase para convertir un objeto Genre a un formato JSON.
    """
    class Meta:
        model = Album
        fields = "__all__"
