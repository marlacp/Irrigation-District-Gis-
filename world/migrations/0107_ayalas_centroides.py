# Generated by Django 3.0.7 on 2021-02-03 21:17

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0106_delete_ayalas_centroides'),
    ]

    operations = [
        migrations.CreateModel(
            name='ayalas_centroides',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=50)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('area', models.FloatField()),
                ('fc', models.FloatField()),
                ('pwp', models.FloatField()),
                ('sat_lv_c', models.FloatField()),
                ('sat_lv_n', models.CharField(max_length=50)),
                ('col_c', models.FloatField()),
                ('col_n', models.CharField(max_length=50)),
                ('prescriptio', models.FloatField()),
                ('agent_c', models.FloatField()),
                ('agent_n', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('irr_mm', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
        ),
    ]