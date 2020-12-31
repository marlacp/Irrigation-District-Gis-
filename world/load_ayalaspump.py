import os
from django.contrib.gis.utils import LayerMapping
from .models import Ayalas_Pump


# Auto-generated `LayerMapping` dictionary for Ayalas_Pump model
ayalas_pump_mapping = {
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



Ayalas_Pump_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/ShapeFinales/shp_PmS/Ayalas_PumpStation/Ayalas_PumpStation_Polygon.shp'))

def run(verbose=True):
    lm= LayerMapping(Ayalas_Pump, Ayalas_Pump_shp, ayalas_pump_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)