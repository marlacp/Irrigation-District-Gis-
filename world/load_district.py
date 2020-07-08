import os
from django.contrib.gis.utils import LayerMapping
from .models import DistrictP


# Auto-generated `LayerMapping` dictionary for DistrictP model
districtp_mapping = {
    'id': 'Id',
    'name': 'NAME',
    'lat': 'LAT',
    'lon': 'LON',
    'area': 'Area',
    'geom': 'MULTIPOLYGON',
}



districtp_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'./DistrictPolygons/District_Polygons.shp'))

def run(verbose=True):
    lm= LayerMapping(DistrictP, districtp_shp, districtp_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)
