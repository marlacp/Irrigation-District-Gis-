

import os
from django.contrib.gis.utils import LayerMapping
from .models import Duitama_Pump

# Auto-generated `LayerMapping` dictionary for Duitama_Pump model
duitama_pump_mapping = {
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
duitama_pump_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/ShapefilexHector/shp_PmS/Duitama_PumpStation/Duitama_PumpStation_Polygon.shp'))

def run(verbose=True):
    lm= LayerMapping(Duitama_Pump, duitama_pump_shp, duitama_pump_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)
