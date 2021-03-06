# Generated by Django 3.0.7 on 2020-12-22 20:10

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0100_delete_districtp'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistrictP',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
