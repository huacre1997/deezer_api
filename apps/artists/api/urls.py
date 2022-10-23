from rest_framework import routers
from .views import ArtistViewSet
from django.urls import path
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('artist', ArtistViewSet)

urlpatterns = router.urls
