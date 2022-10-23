from email.policy import default
from rest_framework.serializers import ModelSerializer
from apps.artists.models import Artist
from rest_framework import serializers
from utils.choices import Type


class ArtistSerializer(serializers.ModelSerializer):
    """
    Clase para convertir un objeto Genre a un formato JSON.
    """
    class Meta:
        model = Artist
        fields = "__all__"
