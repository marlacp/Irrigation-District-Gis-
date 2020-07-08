import os
from django.contrib.gis.utils import LayerMapping
from .models import Countries

countries_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'geom': 'MULTIPOLYGON',
}
country_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'./data/countries.shp'))

def run(verbose=True):
    lm= LayerMapping(Countries, country_shp, countries_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)



