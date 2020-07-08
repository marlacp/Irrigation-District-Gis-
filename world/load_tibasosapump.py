import os
from django.contrib.gis.utils import LayerMapping
from .models import tibasosa_pump

# Auto-generated `LayerMapping` dictionary for tibasosa_pump model
tibasosa_pump_mapping = {
    'id': 'Id',
    'code': 'CODE',
    'lat': 'LAT',
    'lon': 'LON',
    'area': 'AREA',
    'clay': 'CLAY',
    'silt': 'SILT',
    'sand': 'SAND',
    'sp': 'SP',
    'fc': 'FC',
    'pwp': 'PWP',
    'hc': 'HC',
    'density': 'DENSITY',
    'geom': 'MULTIPOLYGON',
}




tibasosa_pump_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Polygon_layers_WGS84-20200625T231731Z-001/Polygon_layers_WGS84/Tibasosa_PumpStation/Tibasosa_PumpStation.shp'))

def run(verbose=True):
    lm= LayerMapping(tibasosa_pump, tibasosa_pump_shp, tibasosa_pump_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)