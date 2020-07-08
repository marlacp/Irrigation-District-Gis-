

import os
from django.contrib.gis.utils import LayerMapping
from .models import Duitama_Pump

# Auto-generated `LayerMapping` dictionary for Duitama_Pump model
duitama_pump_mapping = {
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

duitama_pump_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'./Duitama_Pump/Duitama_PumpStation.shp'))

def run(verbose=True):
    lm= LayerMapping(Duitama_Pump, duitama_pump_shp, duitama_pump_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)
