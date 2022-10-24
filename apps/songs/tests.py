from django.test import TestCase, RequestFactory
from rest_framework.test import force_authenticate
from http import HTTPStatus

from apps.users.models import CustomUser
from apps.songs.api.views import SongViewSet


class SongViewsetTestCase(TestCase):
    # Comando para cargar la data de prueba para los tests
    # python manage.py dumpdata songs > fixtures/songs.json

    # Asignamos los fixtures creados
    fixtures = ["fixtures/songs.json",
                "fixtures/albums.json", "fixtures/artists.json"]

    def setUp(self):
        self.factory = RequestFactory()
        self.user = CustomUser.objects.create_superuser(
            password='123456',
            email='admin@test.com'
        )

    def test_song_search_empty(self):
        '''
            Test del endpoint de búsqueda de canciones sin resultados
        '''
        request = self.factory.get('/song/search', {"q": "aaaa"})
        force_authenticate(request, user=self.user)
        response = SongViewSet.as_view({'get': 'search'})(request)
        # Check if the first dog's name is Balto, like it is in the fixtures:
        self.assertEqual(
            response.data, [])

        self.assertEqual(response.status_code, HTTPStatus.OK._value_)

    def test_song_search(self):
        '''
            Test del endpoint de búsqueda de canciones por param "q"
        '''
        request = self.factory.get('/song/search', {"q": "daft"})
        force_authenticate(request, user=self.user)
        response = SongViewSet.as_view({'get': 'search'})(request)
        # Check if the first dog's name is Balto, like it is in the fixtures:
        self.assertEqual(
            response.data[0]["title"], 'Harder, Better, Faster, Stronger')
        self.assertEqual(
            response.data[0]["artist"]["name"], 'Daft Punk')
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)
