import os
from django.contrib.gis.utils import LayerMapping
from .models import ministerio_Pump

# Auto-generated `LayerMapping` dictionary for ministerio_Pump model
ministerio_pump_mapping = {
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





ministerio_pump_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/ShapefilexHector/shp_PmS/Ministerio_PumpStation/Ministerio_PumpStation_Polygon.shp'))

def run(verbose=True):
    lm= LayerMapping(ministerio_Pump, ministerio_pump_shp, ministerio_pump_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)