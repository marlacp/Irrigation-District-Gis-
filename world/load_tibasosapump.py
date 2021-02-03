import os
from django.contrib.gis.utils import LayerMapping
from .models import tibasosa_pump

# Auto-generated `LayerMapping` dictionary for tibasosa_pump model
tibasosa_pump_mapping = {
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


tibasosa_pump_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Shapes+end/Tibasosa_PumpStation/Tibasosa_PumpStation_Polygon.shp'))

def run(verbose=True):
    lm= LayerMapping(tibasosa_pump, tibasosa_pump_shp, tibasosa_pump_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)