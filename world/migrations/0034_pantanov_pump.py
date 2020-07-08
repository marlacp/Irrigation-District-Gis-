# Generated by Django 3.0.7 on 2020-07-02 20:44

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0033_moniquira_pump'),
    ]

    operations = [
        migrations.CreateModel(
            name='pantanov_pump',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=17)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('area', models.FloatField()),
                ('clay', models.FloatField()),
                ('silt', models.FloatField()),
                ('sand', models.FloatField()),
                ('sp', models.FloatField()),
                ('fc', models.FloatField()),
                ('pwp', models.FloatField()),
                ('hc', models.FloatField()),
                ('density', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
