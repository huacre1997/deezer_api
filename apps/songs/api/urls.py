from rest_framework import routers
from .views import SongViewSet
from django.urls import path
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('song', SongViewSet)

urlpatterns = router.urls
