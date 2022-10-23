from rest_framework import routers
from .views import GenreViewSet, AlbumViewSet
from django.urls import path
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('genre', GenreViewSet)
router.register('album', AlbumViewSet)

urlpatterns = router.urls
