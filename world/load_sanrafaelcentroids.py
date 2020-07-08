import os
from django.contrib.gis.utils import LayerMapping
from .models import sanrafael_centroids

# Auto-generated `LayerMapping` dictionary for sanrafael_centroids model
sanrafael_centroids_mapping = {
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




sanrafael_centroids_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Polygon_layers_WGS84-20200625T231731Z-001/Polygon_layers_WGS84/SanRafael_PumStation/SanRafael_Centroids.shp'))

def run(verbose=True):
    lm= LayerMapping(sanrafael_centroids, sanrafael_centroids_shp, sanrafael_centroids_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)