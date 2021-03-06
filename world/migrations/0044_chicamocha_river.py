# Generated by Django 3.0.7 on 2020-07-13 16:07

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0043_delete_chicamocha_river'),
    ]

    operations = [
        migrations.CreateModel(
            name='chicamocha_river',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('status', models.BigIntegerField()),
                ('length', models.FloatField()),
                ('flow', models.FloatField(blank=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
            ],
        ),
    ]
