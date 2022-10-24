from rest_framework import routers
from .views import GenreViewSet, AlbumViewSet
from django.urls import path
from django.conf.urls import include
app_name = "albums"
router = routers.DefaultRouter()
router.register('genre', GenreViewSet, basename="genre")
router.register('album', AlbumViewSet, basename="album")

urlpatterns = router.urls
