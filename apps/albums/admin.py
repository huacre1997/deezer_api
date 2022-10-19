from django.contrib import admin

from .models import Album, Genre

# Registra el modelo Album en el admin de Django
admin.site.register(Album)

# Registra el modelo Genre en el admin de Django
admin.site.register(Genre)
