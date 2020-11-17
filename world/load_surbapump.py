import os
from django.contrib.gis.utils import LayerMapping
from .models import surba_pump

# Auto-generated `LayerMapping` dictionary for surba_pump model
surba_pump_mapping = {
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


surba_pump_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/ShapefilexHector/shp_PmS/Surba_PumpStation/Surba_PumpStation_Polygon.shp'))

def run(verbose=True):
    lm= LayerMapping(surba_pump, surba_pump_shp, surba_pump_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)