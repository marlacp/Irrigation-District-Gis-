import os
from django.contrib.gis.utils import LayerMapping
from .models import surba_centroids

# Auto-generated `LayerMapping` dictionary for surba_centroids model
surba_centroids_mapping = {
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





surba_centroids_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Polygon_layers_WGS84-20200625T231731Z-001/Polygon_layers_WGS84/Surba_PumpStation/Surba_Centroids.shp'))

def run(verbose=True):
    lm= LayerMapping(surba_centroids, surba_centroids_shp, surba_centroids_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)