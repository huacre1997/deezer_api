from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        # Establece el cifrado hash en la contraseña enviada
        user.set_password(validated_data['password'])

        # Guarda el usuario
        user.save()
        return user
