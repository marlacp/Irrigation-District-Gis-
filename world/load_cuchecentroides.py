import os
from django.contrib.gis.utils import LayerMapping
from .models import cuche_centroides

# Auto-generated `LayerMapping` dictionary for cuche_centroides model
cuche_centroides_mapping = {
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





cuche_centroides_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Polygon_layers_WGS84-20200625T231731Z-001/Polygon_layers_WGS84/Cuche_PumpStation/Cuche_Centroids.shp'))

def run(verbose=True):
    lm= LayerMapping(cuche_centroides, cuche_centroides_shp, cuche_centroides_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)