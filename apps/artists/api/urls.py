from rest_framework import routers
from .views import ArtistViewSet

app_name = "artists"
router = routers.DefaultRouter()
router.register('artist', ArtistViewSet, basename="artist")

urlpatterns = router.urls
