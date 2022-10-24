

# RESTful API - Deezer API



## Overview

Esta aplicación backend es un RestFull API basada en [Deezer API](https://developers.deezer.com/api)

## Content

* [Tech Stack](#techstack)
* [Requeriments](#requirements)
* [Environment Variables](#env)
* [Database Entity Model](#dbmodel)
* Endpoints:
    * [API Login](#login)
    * [API Logout](#logout)
    * [API Register](#register)
    * [API Search song](#search_song)
    * [API Get Album](#get_album)
    * [API Get Artist](#get_artist)
   
## Tech Stack

- **RESTful API:** RESTful API desarrollado en Python con el Framework Django
- **Transactional Database:** PostgreSQL 13.2
- JWT encriptado con clave pública/privada utilizando el algoritmo HS256.


### Comunicación

* Comunicación **HTTPS**.

* El **JWT** generado por la aplicación backend está firmado con una clave privada utilizando
el algoritmo **HS256**.

## Requirements
- Python 3.10.7
- Django 4.1.2
- Django REST Framework 3.14.0

## Instalación
Después de clonar el repositorio, tienes que crear un entorno virtual, para tener una instalación limpia de python.
Puedes hacer esto ejecutando el comando
```
python -m venv env
```

Después de esto, es necesario activar el entorno virtual, puedes obtener más información sobre esto [aquí](https://docs.python.org/3/tutorial/venv.html)

Puedes instalar todas las dependencias necesarias ejecutando
```
pip install -r requirements.txt
```
Una vez instalado todas las dependencias creamos nuestro archivo .env y colocamos nuestras variables de entorno

```bash
# TRANSACTIONAL DATABASE
DATABASE_URL='psql://postgres:123@127.0.0.1:5432/deezer_api'
```
Realizamos las migraciones
```
python manage.py migrate
```
Creamos un superuser
```
python manage.py createsuperuser
```
Ejecutamos el programa
```
python manage.py runserver
```
## Estructura
En una API RESTful, los endpoints (URLs) definen la estructura de la API y cómo los usuarios finales acceden a los datos de nuestra aplicación utilizando los métodos HTTP - GET, POST, PUT, DELETE. Los puntos finales deben organizarse lógicamente en torno a _colecciones_ y _elementos_, que son recursos.

En nuestro caso, tenemos : genr,album,artist,song, por lo que utilizaremos las siguientes URLs - `/song/` y `/song/<id>` ,etc para las colecciones y los elementos, respectivamente:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`artist` | GET | READ | Trae todos los artistas
`artist/:id` | GET | READ | Obtiene un artista
`artist`| POST | CREATE | Crea un nuevo artista
`artist/:id` | PUT | UPDATE | Actualiza un artista
`artist/:id/desactivate/` | PUT | UPDATE  | Elimina de manera lógica un artista cambiando su estado a False
`artist/:id/restore/` | PUT | UPDATE | Restaura un artista eliminado cambiando su estado a True

## Endpoints
<a name="login"></a>
### Endpoint: Login

```
POST /login
```

Este endpoint es usado para el login de usuario

Body:

```json
{
    "email": "admin@gmail.com",
    "password": "123456"
}
```

Response:

```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY2NjcyMTA3LCJpYXQiOjE2NjY1ODU3MDcsImp0aSI6Ijk3OGYxZWMxMTI5NTRhZDdiNjA3YmY3OTVmMzA3M2U4IiwidXNlcl9pZCI6NH0.Xr-tF-3yIZYLPwRXqp-O-5G9IJPMIkJJOJXf4yRQmW4",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NDM2MTcwNywiaWF0IjoxNjY2NTg1NzA3LCJqdGkiOiIwMWJjNDgxNWFkZDE0YWNiODIxYzg0Zjc0MmU0NzRlMiIsInVzZXJfaWQiOjR9.ZBBf4vwxZJhwqTSJi2z1a3uLxYgNM3c0qu5k8vA8qwQ"
}
```

Si la autenticación tiene éxito, se devuelve un JWT en la directiva "Authorization" de la cabecera de respuesta. Este JWT es necesario para utilizar los endpoints que consisten en manipular información.

El JWT tiene un tiempo de expiración de 1 día

Example JWT:

```
Authorization: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InV1aWQiOjEsImVtYWlsIjoibWFya2V0aW5nQHN0b3JlLmNvbSIsIm5hbWUiOiJVc2VyIE1hcmtldGluZyJ9LCJ0aW1lc3RhbXAiOjE2NjIyMjk2NDgxMzIsImlhdCI6MTY2MjIyOTY0OCwiZXhwIjoxNjYyMjMzMjQ4fQ.m_q5NxgJnLaUG5OB_zqeWIZhI3cJ8q_OqU1MqBjU-sePheKfPwZCqi-oYi52RjxQAbQYdRo3tRvdggAGHYVg5JTWr2AzKnQf2gA2XrkLSsN0Zibj2ERbYEANZm5FjmHLWQkzkagqgkrDfoaY0eIAoncZfCeilLfrVBSDa84aw0X8XXFV-j3BF6LdX1XiSs-7CNj_4bp72Q2KgmTioXUAdA9KApue39FYWz7lcnoWrw4lMaXDw_w8qeq1B49USPY7_Lth8VEdNGjI7FgwZgudTAwvRnOAnP4Vz72FOrUI2Pp6jGhzN1UNAZB35y5Pbh9CdA2PirrroJeX9vh8xIx8srFoKag2emkdqL5BfmjLLZq_k20BM9BH403153fc78OLlCh-XlVuVkA2AS4IMApFGR1sNIPteln_kdDoJlsvNaoq1jwMQ_Q5g2cmAK7SzEAMMUElkpD8NoUE91R5abXnXOj9erVlOezT3C7-c-zSSbeM4-FhypbEIDLs0m9X8HfTDNW9wPzkN7S1NtP6jWvwKVQl_JPqtzAdyMNqmpsEE2HBpJqe6rwhfmvUntUc85MMTK2OHcTBT-NJ352Mqk7UGVD_cgXDx-kT67MaoPWozgeLtHjRRNp8oo70ZEIhn20Dqo7aGMBXLca1dmDJUnbwhLVTqk9oqpBN0kEywunClAU
```
<a name="logout"></a>
### Endpoint: Logout

```
POST /v1/auth
```

Este endpoint es usado para el logout

Body:

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NDM2MTcwNywiaWF0IjoxNjY2NTg1NzA3LCJqdGkiOiIwMWJjNDgxNWFkZDE0YWNiODIxYzg0Zjc0MmU0NzRlMiIsInVzZXJfaWQiOjR9.ZBBf4vwxZJhwqTSJi2z1a3uLxYgNM3c0qu5k8vA8qwQ",
}
```

Response:

```json
{
    "message": "Successful logout"
}
```
<a name="register"></a>
### Endpoint: Register

```
POST /register
```

Este endpoint es usado para registrar usuarios.

Body:

```json
{
    "email":"test@gmail.com",
    "password":"123456",
    "confirm_password":"123456",
    "country":"Perú",
    "first_name":"Test",
}
```

Response:

```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY2NjczNTI1LCJpYXQiOjE2NjY1ODcxMjUsImp0aSI6IjkzODE2OGQwZTc1YTQ3NzQ5NzQ1YmZlNTgyYjhkYTk0IiwidXNlcl9pZCI6MjJ9.wnkkggDkuTXa1OuCmGgh62clT1ldQR16JyKZ2zFIigQ",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NDM2MzEyNSwiaWF0IjoxNjY2NTg3MTI1LCJqdGkiOiI1NDVjMTQ0MjhjM2M0YWI5OGU3MTg2MjMyMTVhOGY1YSIsInVzZXJfaWQiOjIyfQ.eSLQ_SA7mgDtTJfCADjKzvFs6UDukLHN0HG-87Gm-LA",
    "user": {
        "email": "test@gmail.com",
        "first_name": "Test",
        "country": "Perú"
    }
}
```
<a name="search_song"></a>
### Endpoint: Search song

```
GET /song/search/?q=daft
```
Este endpoint es usado para buscar una canción tomando como referencia su título o el nombre de un artista

Response:

```json
[
    {
        "id": 1,
        "title": "Harder, Better, Faster, Stronger",
        "title_short": "Harder, Better, Faster, Stronger",
        "link": "https://www.deezer.com/track/3135556",
        "duration": 224,
        "track_position": 4,
        "disk_number": 1,
        "rank": 770049,
        "release_date": "2005-01-24",
        "type": "track",
        "artist": {
            "id": 1,
            "name": "Daft Punk",
            "link": "https://www.deezer.com/artist/27",
            "picture": "https://api.deezer.com/artist/27/image",
            "nb_album": 31,
            "nb_fan": 4348083,
            "radio": true,
            "type": "artist"
        },
        "album": {
            "id": 1,
            "title": "Discovery",
            "link": "https://www.deezer.com/album/302127",
            "label": "Daft Life Ltd./ADA France",
            "nb_tracks": 14,
            "release_data": "2001-03-07",
            "duration": 3660,
            "fans": 263506,
            "available": true,
            "type": "album",
            "artist": {
                "id": 1,
                "name": "Daft Punk",
                "link": "https://www.deezer.com/artist/27",
                "picture": "https://api.deezer.com/artist/27/image",
                "nb_album": 31,
                "nb_fan": 4348083,
                "radio": true,
                "type": "artist"
            },
            "genre": {
                "id": 3,
                "picture": "https://api.deezer.com/genre/113/image",
                "name": "Dance",
                "type": "genre"
            }
        }
    },
    {
        "id": 2,
        "title": "One More Time",
        "title_short": "One More Time",
        "link": "https://www.deezer.com/track/3135553",
        "duration": 3,
        "track_position": 3,
        "disk_number": 2,
        "rank": 686171,
        "release_date": "2005-01-24",
        "type": "track",
        "artist": {
            "id": 1,
            "name": "Daft Punk",
            "link": "https://www.deezer.com/artist/27",
            "picture": "https://api.deezer.com/artist/27/image",
            "nb_album": 31,
            "nb_fan": 4348083,
            "radio": true,
            "type": "artist"
        },
        "album": {
            "id": 1,
            "title": "Discovery",
            "link": "https://www.deezer.com/album/302127",
            "label": "Daft Life Ltd./ADA France",
            "nb_tracks": 14,
            "release_data": "2001-03-07",
            "duration": 3660,
            "fans": 263506,
            "available": true,
            "type": "album",
            "artist": {
                "id": 1,
                "name": "Daft Punk",
                "link": "https://www.deezer.com/artist/27",
                "picture": "https://api.deezer.com/artist/27/image",
                "nb_album": 31,
                "nb_fan": 4348083,
                "radio": true,
                "type": "artist"
            },
            "genre": {
                "id": 3,
                "picture": "https://api.deezer.com/genre/113/image",
                "name": "Dance",
                "type": "genre"
            }
        }
    }
]
```
<a name="get_album"></a>
### Endpoint: Get Album
```
GET /album/1/
```
Endpoint usado para traer un album con su id

Response:
```json
{
    "id": 1,
    "title": "Discovery",
    "link": "https://www.deezer.com/album/302127",
    "label": "Daft Life Ltd./ADA France",
    "nb_tracks": 14,
    "release_data": "2001-03-07",
    "duration": 3660,
    "fans": 263506,
    "available": true,
    "type": "album",
    "artist": {
        "id": 1,
        "name": "Daft Punk",
        "link": "https://www.deezer.com/artist/27",
        "picture": "https://api.deezer.com/artist/27/image",
        "nb_album": 31,
        "nb_fan": 4348083,
        "radio": true,
        "type": "artist"
    },
    "genre": {
        "id": 3,
        "picture": "https://api.deezer.com/genre/113/image",
        "name": "Dance",
        "type": "genre"
    }
}
```
<a name="get_artist"></a>
### Endpoint: Get Artist
```
GET /artist/1/
```
Endpoint usado para traer un artista con su id.

Response:


```json
{
    "id": 1,
    "name": "Daft Punk",
    "link": "https://www.deezer.com/artist/27",
    "picture": "https://api.deezer.com/artist/27/image",
    "nb_album": 31,
    "nb_fan": 4348083,
    "radio": true,
    "type": "artist"
}
```

Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs