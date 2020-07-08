import os
from django.contrib.gis.utils import LayerMapping
from .models import duitama_centroides

# Auto-generated `LayerMapping` dictionary for duitama_centroides model
duitama_centroides_mapping = {
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




duitama_centroides_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Polygon_layers_WGS84-20200625T231731Z-001/Polygon_layers_WGS84/Duitama_PumpStation/Duitama_Centroids.shp'))

def run(verbose=True):
    lm= LayerMapping(duitama_centroides, duitama_centroides_shp, duitama_centroides_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)