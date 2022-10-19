# Generated by Django 4.1.2 on 2022-10-19 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de modificación')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Nombre')),
                ('picture', models.URLField(null=True, verbose_name='Url')),
                ('type', models.CharField(choices=[('genre', 'Género'), ('track', 'Canción'), ('album', 'Album'), ('artist', 'Artista')], default=None, max_length=10, verbose_name='Tipo')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genrs',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de modificación')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Título')),
                ('link', models.URLField(null=True, verbose_name='Link')),
                ('label', models.CharField(max_length=50, verbose_name='Label')),
                ('nb_tracks', models.SmallIntegerField(null=True, verbose_name='Número de tracks')),
                ('release_data', models.DateField(null=True, verbose_name='Fecha de lanzamiento')),
                ('duration', models.IntegerField(null=True, verbose_name='Duración')),
                ('fans', models.IntegerField(null=True, verbose_name='Fans')),
                ('available', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('genre', 'Género'), ('track', 'Canción'), ('album', 'Album'), ('artist', 'Artista')], default=None, max_length=10, verbose_name='Tipo')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist_album', to='artists.artist', verbose_name='Artista')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre_album', to='albums.genre', verbose_name='Género')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
        ),
    ]