import os
from django.contrib.gis.utils import LayerMapping
from .models import ayalas_centroides

# Auto-generated `LayerMapping` dictionary for ayalas_centroides model
ayalas_centroides_mapping = {
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





ayalas_centroides_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Polygon_layers_WGS84-20200625T231731Z-001/Polygon_layers_WGS84/Ayalas_PumpStation/Ayalas_Centroids.shp'))

def run(verbose=True):
    lm= LayerMapping(ayalas_centroides, ayalas_centroides_shp, ayalas_centroides_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)