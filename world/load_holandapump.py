import os
from django.contrib.gis.utils import LayerMapping
from .models import Holanda_Pump

# Auto-generated `LayerMapping` dictionary for Holanda_Pump model
holanda_pump_mapping = {
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


holanda_pump_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Polygon_layers_WGS84-20200625T231731Z-001/Polygon_layers_WGS84/Holanda_PumpStation/Holanda_PumpStation.shp'))

def run(verbose=True):
    lm= LayerMapping(Holanda_Pump, holanda_pump_shp, holanda_pump_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)



