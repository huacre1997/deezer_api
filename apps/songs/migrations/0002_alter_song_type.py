# Generated by Django 4.1.2 on 2022-10-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='type',
            field=models.CharField(default='track', max_length=10, verbose_name='Tipo'),
        ),
    ]
