from apps.users.models import CustomUser
from rest_framework import serializers
from django.utils.text import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=70, min_length=6, write_only=True)
    confirm_password = serializers.CharField(
        max_length=70, min_length=6, write_only=True)
    first_name = serializers.CharField(
        max_length=50)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'password', 'confirm_password',
                  'country']

    def validate_email(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise serializers.ValidationError('Email invalid')
        return email

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError(
                'Passwords must be the same')

        return data

    def create(self, validated_data):
        # Removemos el confirm_password de validated_data
        del validated_data['confirm_password']

        user = CustomUser(**validated_data)
        # Hashea su password
        user.set_password(validated_data['password'])
        # Guarda el usuario
        user.save()
        return user


class LogoutSerializer(serializers.Serializer):

    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Invalid token or expired')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            # Pasamos el refresh token 
            token = RefreshToken(self.token)

            # Envía el refresh token a la tabla Black List donde no volverá a ser válido o utilizado
            token.blacklist()

        except TokenError:
            self.fail('bad_token')
