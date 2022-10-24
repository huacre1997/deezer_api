from django.test import TestCase, RequestFactory
from django.urls import reverse
from rest_framework.test import force_authenticate
from http import HTTPStatus

from apps.users.models import CustomUser
from apps.artists.api.views import ArtistViewSet


class SongViewsetTestCase(TestCase):
    # Comando para cargar la data de prueba para los tests
    # python manage.py dumpdata songs > fixtures/artists.json

    # Asignamos los fixtures creados
    fixtures = ["fixtures/artists.json"]

    def setUp(self):
        self.factory = RequestFactory()
        self.user = CustomUser.objects.create_superuser(
            password='123456',
            email='admin@test.com'
        )

    def test_get_artist(self):
        '''
        Test que trae la info de un artista con su pk
        '''
        url_retrieve = reverse("artists:artist-detail", kwargs={"pk": 1})
        request = self.factory.get(url_retrieve)
        force_authenticate(request, user=self.user)
        response = ArtistViewSet.as_view({'get': 'retrieve'})(request, pk=1)
        self.assertEqual(
            response.data["name"], 'Daft Punk')
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)
