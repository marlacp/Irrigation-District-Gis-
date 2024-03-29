import os
from django.contrib.gis.utils import LayerMapping
from .models import Holanda_Pump

# Auto-generated `LayerMapping` dictionary for Holanda_Pump model
holanda_pump_mapping = {
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
    'irr_mm': 'IRR_MM',
    'geom': 'MULTIPOLYGON',
}



holanda_pump_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Shapes+end/Holanda_PumpStation/Holanda_PumpStation_Polygon.shp'))

def run(verbose=True):
    lm= LayerMapping(Holanda_Pump, holanda_pump_shp, holanda_pump_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)



