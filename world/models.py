from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models as gis_models
from django.db.models import Manager as GeoManager
from django.contrib.gis.db.models import PointField #, GeoManager
from django.db.models import Manager as GeoManager

# Create your models here.
class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = PointField(srid=4326)
    objects = GeoManager()
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural="Incidences"   


class Countries(models.Model):
    fips = gis_models.CharField(max_length=2)
    iso2 = gis_models.CharField(max_length=2)
    iso3 = gis_models.CharField(max_length=3)
    un = gis_models.IntegerField()
    name = models.CharField(max_length=50)
    area = gis_models.IntegerField()
    pop2005 = gis_models.BigIntegerField()
    region = models.IntegerField()
    subregion = gis_models.IntegerField()
    lon = gis_models.FloatField()
    lat = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)
    #objects = GeoManager()
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural="Countries"  

class DistrictP(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    name = gis_models.CharField(max_length=80)
    lat = gis_models.FloatField()
    lon = gis_models.FloatField()
    area = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)
    def __unicode__(self):
        return self.name

class Duitama_Pump(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=50)
    lon = gis_models.FloatField()
    lat = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    ks = gis_models.FloatField()
    prescriptio = gis_models.FloatField()
    crop_n = gis_models.CharField(max_length=50)
    crop_c = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)
    def __unicode__(self):
        return self.code

class Ayalas_Pump(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=50)
    lon = gis_models.FloatField()
    lat = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    ks = gis_models.FloatField()
    prescriptio = gis_models.FloatField()
    crop_n = gis_models.CharField(max_length=50)
    crop_c = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)
    def __unicode__(self):
        return self.code

class Cuche_Pump(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=50)
    lon = gis_models.FloatField()
    lat = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    ks = gis_models.FloatField()
    prescriptio = gis_models.FloatField()
    crop_n = gis_models.CharField(max_length=50)
    crop_c = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)
    def __unicode__(self):
        return self.code

class Holanda_Pump(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=50)
    lon = gis_models.FloatField()
    lat = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    ks = gis_models.FloatField()
    prescriptio = gis_models.FloatField()
    crop_n = gis_models.CharField(max_length=50)
    crop_c = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)
    def __unicode__(self):
        return self.code

class Lasvueltas_Pump(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=50)
    lon = gis_models.FloatField()
    lat = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    ks = gis_models.FloatField()
    prescriptio = gis_models.FloatField()
    crop_n = gis_models.CharField(max_length=50)
    crop_c = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)
    def __unicode__(self):
        return self.code

class ministerio_Pump(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=50)
    lon = gis_models.FloatField()
    lat = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    ks = gis_models.FloatField()
    prescriptio = gis_models.FloatField()
    crop_n = gis_models.CharField(max_length=50)
    crop_c = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)
    def __unicode__(self):
        return self.code

class moniquira_Pump(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=50)
    lon = gis_models.FloatField()
    lat = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    ks = gis_models.FloatField()
    prescriptio = gis_models.FloatField()
    crop_n = gis_models.CharField(max_length=50)
    crop_c = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)
    def __unicode__(self):
        return self.code

class pantanov_pump(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=50)
    lon = gis_models.FloatField()
    lat = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    ks = gis_models.FloatField()
    prescriptio = gis_models.FloatField()
    crop_n = gis_models.CharField(max_length=50)
    crop_c = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)
    def __unicode__(self):
        return self.code

class sanrafael_pump(models.Model):
    id = gis_models.IntegerField(primary_key=True)
    code = gis_models.CharField(max_length=50)
    lon = gis_models.FloatField()
    lat = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    ks = gis_models.FloatField()
    prescriptio = gis_models.FloatField()
    crop_n = gis_models.CharField(max_length=50)
    crop_c = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)
    def __unicode__(self):
        return self.code

class surba_pump(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=50)
    lon = gis_models.FloatField()
    lat = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    ks = gis_models.FloatField()
    prescriptio = gis_models.FloatField()
    crop_n = gis_models.CharField(max_length=50)
    crop_c = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)
    def __unicode__(self):
        return self.code

class tibasosa_pump(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=50)
    lon = gis_models.FloatField()
    lat = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    ks = gis_models.FloatField()
    prescriptio = gis_models.FloatField()
    crop_n = gis_models.CharField(max_length=50)
    crop_c = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)
    def __unicode__(self):
        return self.code

class ayalas_centroides(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=9)
    lat = gis_models.FloatField()
    lon = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    sp = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    hc = gis_models.FloatField()
    density = gis_models.FloatField()
    geom = gis_models.MultiPointField(srid=4326)
    def __unicode__(self):
        return self.code

class cuche_centroides(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=9)
    lat = gis_models.FloatField()
    lon = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    sp = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    hc = gis_models.FloatField()
    density = gis_models.FloatField()
    geom = gis_models.MultiPointField(srid=4326)
    def __unicode__(self):
        return self.code

class duitama_centroides(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=20)
    lat = gis_models.FloatField()
    lon = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    sp = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    hc = gis_models.FloatField()
    density = gis_models.FloatField()
    geom = gis_models.MultiPointField(srid=4326)
    def __unicode__(self):
        return self.code


class holanda_centroids(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=11)
    lat = gis_models.FloatField()
    lon = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    sp = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    hc = gis_models.FloatField()
    density = gis_models.FloatField()
    geom = gis_models.MultiPointField(srid=4326)
    def __unicode__(self):
        return self.code


class lasvueltas_centroids(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=20)
    lat = gis_models.FloatField()
    lon = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    sp = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    hc = gis_models.FloatField()
    density = gis_models.FloatField()
    geom = gis_models.MultiPointField(srid=4326)
    def __unicode__(self):
        return self.code


class ministerio_centroids(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=14)
    lat = gis_models.FloatField()
    lon = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    sp = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    hc = gis_models.FloatField()
    density = gis_models.FloatField()
    geom = gis_models.MultiPointField(srid=4326)
    def __unicode__(self):
        return self.code


class moniquira_centroids(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=20)
    lat = gis_models.FloatField()
    lon = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    sp = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    hc = gis_models.FloatField()
    density = gis_models.FloatField()
    geom = gis_models.MultiPointField(srid=4326)
    def __unicode__(self):
        return self.code


class pantanov_centroids(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=17)
    lat = gis_models.FloatField()
    lon = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    sp = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    hc = gis_models.FloatField()
    density = gis_models.FloatField()
    geom = gis_models.MultiPointField(srid=4326)
    def __unicode__(self):
        return self.code


class sanrafael_centroids(models.Model):
    id = gis_models.IntegerField(primary_key=True)
    code = gis_models.CharField(max_length=20)
    lat = gis_models.FloatField()
    lon = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    sp = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    hc = gis_models.FloatField()
    density = gis_models.FloatField()
    geom = gis_models.MultiPointField(srid=4326)
    def __unicode__(self):
        return self.code


class surba_centroids(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=9)
    lat = gis_models.FloatField()
    lon = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    sp = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    hc = gis_models.FloatField()
    density = gis_models.FloatField()
    geom = gis_models.MultiPointField(srid=4326)
    def __unicode__(self):
        return self.code


class tibasosa_centroids(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    code = gis_models.CharField(max_length=12)
    lat = gis_models.FloatField()
    lon = gis_models.FloatField()
    area = gis_models.FloatField()
    clay = gis_models.FloatField()
    silt = gis_models.FloatField()
    sand = gis_models.FloatField()
    sp = gis_models.FloatField()
    fc = gis_models.FloatField()
    pwp = gis_models.FloatField()
    hc = gis_models.FloatField()
    density = gis_models.FloatField()
    geom = gis_models.MultiPointField(srid=4326)
    def __unicode__(self):
        return self.code

class chicamocha_river(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    name = gis_models.CharField(max_length=30)
    status = gis_models.BigIntegerField()
    length = gis_models.FloatField()
    flow = gis_models.FloatField(null=True)
    geom = gis_models.MultiLineStringField(srid=4326)
    def __unicode__(self):
        return self.name

class reservoirs(models.Model):
    id = gis_models.BigIntegerField(primary_key=True)
    name = gis_models.CharField(max_length=80)
    status = gis_models.FloatField()
    level = gis_models.FloatField(null=True)
    area = gis_models.FloatField()
    lat = gis_models.FloatField()
    lon = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)
    def __unicode__(self):
        return self.name