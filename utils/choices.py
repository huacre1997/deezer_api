from django.db import models
# link gettext - > https://docs.djangoproject.com/en/4.1/topics/i18n/translation/
from django.utils.translation import gettext as _

# _("") -> Utilizado para poder traducir a otros idiomas


class Type(models.TextChoices):
    GENRE = "genre", _("Género")
    SONG = "track", _("Canción")
    ALBUM = "album", _("Album")
    ARTIST = "artist", _("Artista")
