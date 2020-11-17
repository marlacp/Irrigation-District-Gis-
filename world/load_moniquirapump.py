import os
from django.contrib.gis.utils import LayerMapping
from .models import moniquira_Pump

# Auto-generated `LayerMapping` dictionary for moniquira_Pump model
moniquira_pump_mapping = {
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




moniquira_pump_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/ShapefilexHector/shp_PmS/Monquira_PumpStation/Monquira_PumpStation_Polygon.shp'))

def run(verbose=True):
    lm= LayerMapping(moniquira_Pump, moniquira_pump_shp, moniquira_pump_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)