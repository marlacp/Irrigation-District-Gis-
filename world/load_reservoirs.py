import os
from django.contrib.gis.utils import LayerMapping
from .models import reservoirs

# Auto-generated `LayerMapping` dictionary for reservoirs model
reservoirs_mapping = {
    'id': 'id',
    'name': 'Name',
    'status': 'Status',
    'level': 'Level',
    'area': 'Area',
    'lat': 'LAT',
    'lon': 'LON',
    'geom': 'MULTIPOLYGON',
}




reservoirs_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Polygon_layers_WGS84-20200625T231731Z-001/Polygon_layers_WGS84/Reservoirs_Source/Reservoirs_Source.shp'))

def run(verbose=True):
    lm= LayerMapping(reservoirs, reservoirs_shp, reservoirs_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)