import os
from django.contrib.gis.utils import LayerMapping
from .models import moniquira_Pump

# Auto-generated `LayerMapping` dictionary for moniquira_Pump model
moniquira_pump_mapping = {
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




moniquira_pump_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Polygon_layers_WGS84-20200625T231731Z-001/Polygon_layers_WGS84/Monquira_PumpStation/Monquira_PumpStation.shp'))

def run(verbose=True):
    lm= LayerMapping(moniquira_Pump, moniquira_pump_shp, moniquira_pump_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)