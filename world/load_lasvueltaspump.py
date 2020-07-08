import os
from django.contrib.gis.utils import LayerMapping
from .models import Lasvueltas_Pump

# Auto-generated `LayerMapping` dictionary for Lasvueltas_Pump model
lasvueltas_pump_mapping = {
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



lasvueltas_pump_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Polygon_layers_WGS84-20200625T231731Z-001/Polygon_layers_WGS84/Las_Vueltas_PumpStation/Las_Vueltas_PumpStation.shp'))

def run(verbose=True):
    lm= LayerMapping(Lasvueltas_Pump, lasvueltas_pump_shp, lasvueltas_pump_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)