from django.db import models
# link gettext - > https://docs.djangoproject.com/en/4.1/topics/i18n/translation/
from django.utils.translation import gettext as _
from utils.base.models import ModelBase
from utils.choices import Type


# _("") -> Utilizado para poder traducir a otros idiomas

class Artist(ModelBase):
    name = models.CharField(max_length=50, null=False,
                            blank=False, verbose_name=_("Nombre"))
    link = models.URLField(max_length=200, null=False,
                           blank=False, verbose_name=_("Link"))
    picture = models.URLField(
        max_length=200, null=False, blank=False, verbose_name=_("Foto"))
    nb_album = models.SmallIntegerField(
        null=False, blank=False, verbose_name=_("Número de álbum"))
    nb_fan = models.IntegerField(
        null=False, blank=False, verbose_name=_("Número de fans"))
    radio = models.BooleanField(default=True, verbose_name=_("Radio"))
    type = models.CharField(max_length=10, null=False, default=Type.ARTIST, blank=False,
                            verbose_name=_("Tipo"))

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
        verbose_name = "Artist"

        # Texto que aparecerá en nuestra aplicación en plural.
        verbose_name_plural = "Artists"
