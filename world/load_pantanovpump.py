import os
from django.contrib.gis.utils import LayerMapping
from .models import pantanov_pump

# Auto-generated `LayerMapping` dictionary for pantanov_pump model
pantanov_pump_mapping = {
    'id': 'ID',
    'code': 'CODE',
    'lon': 'LON',
    'lat': 'LAT',
    'area': 'AREA',
    'clay': 'CLAY',
    'silt': 'SILT',
    'sand': 'SAND',
    'fc': 'FC',
    'pwp': 'PWP',
    'ks': 'KS',
    'prescriptio': 'PRESCRIPTIO',
    'crop_n': 'CROP_N',
    'crop_c': 'CROP_C',
    'geom': 'MULTIPOLYGON',
}


pantanov_pump_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/ShapeFinales/shp_PmS/Pantano_PumpStation/Pantano_PumpStation_Polygon.shp'))

def run(verbose=True):
    lm= LayerMapping(pantanov_pump, pantanov_pump_shp, pantanov_pump_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)