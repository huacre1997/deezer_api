from rest_framework import routers
from .views import SongViewSet

router = routers.DefaultRouter()
router.register('song', SongViewSet)

urlpatterns = router.urls
