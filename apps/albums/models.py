from django.db import models
# link gettext - > https://docs.djangoproject.com/en/4.1/topics/i18n/translation/
from django.utils.translation import gettext as _

from utils.models import ModelBase
from utils.choices import Type

from apps.artists.models import Artist


# _("") -> Utilizado para poder traducir a otros idiomas
class Genre(ModelBase):
    name = models.CharField(
        max_length=100, blank=False, null=True, verbose_name=_("Nombre"))
    picture = models.URLField(max_length=200, blank=False,
                              null=True, verbose_name=_("Url"))
    type = models.CharField(max_length=10, null=False, default=None, blank=False,
                            choices=Type.choices, verbose_name=_("Tipo"))

    def __str__(self):
        """
        Método para devolver un string que represente al objeto
        """
        return self.name

    class Meta:
        """
        Clase Meta:
        Clase de Django para agregar opciones adicionales a nuestro modelo.
        Link: https://docs.djangoproject.com/en/4.1/ref/models/options/
        """
        # Texto que aparecerá en nuestra aplicación.
        verbose_name = "Genre"

        # Texto que aparecerá en nuestra aplicación en plural.
        verbose_name_plural = "Genrs"


class Album(ModelBase):
    title = models.CharField(
        max_length=100, blank=False, null=True, verbose_name=_("Título"))
    link = models.URLField(max_length=200, blank=False,
                           null=True, verbose_name=_("Link"))
    label = models.CharField(max_length=50, null=False,
                             blank=False, verbose_name=_("Label"))
    nb_tracks = models.SmallIntegerField(
        blank=False, null=True, verbose_name=_("Número de tracks"))
    release_data = models.DateField(
        blank=False, null=True, verbose_name=_("Fecha de lanzamiento"))
    duration = models.IntegerField(
        blank=False, null=True, verbose_name=_("Duración"))
    fans = models.IntegerField(
        blank=False, null=True, verbose_name=_("Fans"))
    available = models.BooleanField(default=True)
    artist = models.ForeignKey(Artist, null=False, blank=False, related_name="artist_album", on_delete=models.CASCADE, verbose_name=_(
        "Artista"))
    genre = models.ForeignKey(Genre, null=False, blank=False, related_name="genre_album", on_delete=models.CASCADE, verbose_name=_(
        "Género"))
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
        verbose_name = "Album"

        # Texto que aparecerá en nuestra aplicación en plural.
        verbose_name_plural = "Albums"
        