import os
from django.contrib.gis.utils import LayerMapping
from .models import tibasosa_centroids

# Auto-generated `LayerMapping` dictionary for tibasosa_centroids model
tibasosa_centroids_mapping = {
    'id': 'ID',
    'code': 'CODE',
    'lon': 'LON',
    'lat': 'LAT',
    'area': 'AREA',
    'fc': 'FC',
    'pwp': 'PWP',
    'sat_lv_c': 'SAT_LV_C',
    'sat_lv_n': 'SAT_LV_N',
    'col_c': 'COL_C',
    'col_n': 'COL_N',
    'prescriptio': 'PRESCRIPTIO',
    'agent_c': 'AGENT_C',
    'agent_n': 'AGENT_N',
    'model': 'MODEL',
    'geom': 'MULTIPOINT',
}

tibasosa_centroids_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/ShapefilexHector/shp_PmS/Tibasosa_PumpStation/Tibasosa_PumpStation_Centroids.shp'))

def run(verbose=True):
    lm= LayerMapping(tibasosa_centroids, tibasosa_centroids_shp, tibasosa_centroids_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)