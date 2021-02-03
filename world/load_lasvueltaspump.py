import os
from django.contrib.gis.utils import LayerMapping
from .models import Lasvueltas_Pump

# Auto-generated `LayerMapping` dictionary for Lasvueltas_Pump model
lasvueltas_pump_mapping = {
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




lasvueltas_pump_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Shapes+end/LasVueltas_PumpStation/LasVueltas_PumpStation_Polygon.shp'))

def run(verbose=True):
    lm= LayerMapping(Lasvueltas_Pump, lasvueltas_pump_shp, lasvueltas_pump_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)