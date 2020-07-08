import os
from django.contrib.gis.utils import LayerMapping
from .models import Ayalas_Pump


# Auto-generated `LayerMapping` dictionary for Ayalas_Pump model
ayalas_pump_mapping = {
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



Ayalas_Pump_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Polygon_layers_WGS84-20200625T231731Z-001/Polygon_layers_WGS84/Ayalas_PumpStation/Ayalas_PumpStation.shp'))

def run(verbose=True):
    lm= LayerMapping(Ayalas_Pump, Ayalas_Pump_shp, ayalas_pump_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)