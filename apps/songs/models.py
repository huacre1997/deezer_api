from django.db import models
# link gettext - > https://docs.djangoproject.com/en/4.1/topics/i18n/translation/
from django.utils.translation import gettext as _
from utils.choices import Type
from utils.models import ModelBase
from apps.artists.models import Artist
from apps.albums.models import Album

# _("") -> Utilizado para poder traducir a otros idiomas


class Song(ModelBase):
    title = models.CharField(max_length=200, null=True,
                             blank=True, verbose_name=_("Título"))
    title_short = models.CharField(max_length=200, null=True,
                                   blank=True, verbose_name=_("Título corto"))
    link = models.URLField(max_length=200, verbose_name=_("Link"))
    duration = models.SmallIntegerField(null=True,
                                        blank=True, verbose_name=_("Tiempo de duración"))
    track_position = models.SmallIntegerField(null=True,
                                              blank=True, verbose_name=_("Posición"))
    disk_number = models.SmallIntegerField(null=True,
                                           blank=True, verbose_name=_("Número de disco"))
    rank = models.IntegerField(null=True,
                               blank=True, verbose_name=_("Rank"))
    release_date = models.DateField(null=True,
                                    blank=True, verbose_name=_("Fecha de lanzamiento"))
    artist = models.ForeignKey(Artist, blank=False, null=False, related_name="song_artist", on_delete=models.CASCADE, verbose_name=_(
        "Artista"))
    album = models.ForeignKey(Album, blank=False, null=False, related_name="album_artist", on_delete=models.CASCADE, verbose_name=_(
        "Album"))
    type = models.CharField(max_length=10, null=False, default=None, blank=False,
                            choices=Type.choices, verbose_name=_("Tipo"))

    def __str__(self):
        """
        Método para devolver un string que represente al objeto
        """
        return self.title

    class Meta:
        """
        Clase Meta:
        Clase de Django para agregar opciones adicionales a nuestro modelo.
        Link: https://docs.djangoproject.com/en/4.1/ref/models/options/
        """
        # Texto que aparecerá en nuestra aplicación.
        verbose_name = "Song"

        # Texto que aparecerá en nuestra aplicación en plural.
        verbose_name_plural = "Songs"
