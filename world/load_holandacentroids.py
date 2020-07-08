import os
from django.contrib.gis.utils import LayerMapping
from .models import holanda_centroids

# Auto-generated `LayerMapping` dictionary for holanda_centroids model
holanda_centroids_mapping = {
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
    'geom': 'MULTIPOINT',
}




holanda_centroids_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Polygon_layers_WGS84-20200625T231731Z-001/Polygon_layers_WGS84/Holanda_PumpStation/Holanda_Centroids.shp'))

def run(verbose=True):
    lm= LayerMapping(holanda_centroids, holanda_centroids_shp, holanda_centroids_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)