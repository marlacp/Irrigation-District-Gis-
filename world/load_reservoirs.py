import os
from django.contrib.gis.utils import LayerMapping
from .models import reservoirs

# Auto-generated `LayerMapping` dictionary for reservoirs model
reservoirs_mapping = {
    'id': 'ID',
    'name': 'NAME',
    'status': 'STATUS',
    'level': 'LEVEL',
    'area': 'AREA',
    'lat': 'LAT',
    'lon': 'LON',
    'geom': 'MULTIPOLYGON',
}




reservoirs_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/ShapeFinales/shp_PmS/Reservoirs_Source/Reservoirs_Source_Polygon.shp'))

def run(verbose=True):
    lm= LayerMapping(reservoirs, reservoirs_shp, reservoirs_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)