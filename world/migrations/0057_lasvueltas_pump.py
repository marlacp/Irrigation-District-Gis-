# Generated by Django 3.0.7 on 2020-11-16 22:37

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0056_delete_lasvueltas_pump'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lasvueltas_Pump',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=50)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('area', models.FloatField()),
                ('clay', models.FloatField()),
                ('silt', models.FloatField()),
                ('sand', models.FloatField()),
                ('fc', models.FloatField()),
                ('pwp', models.FloatField()),
                ('ks', models.FloatField()),
                ('prescriptio', models.FloatField()),
                ('crop_n', models.CharField(max_length=50)),
                ('crop_c', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
