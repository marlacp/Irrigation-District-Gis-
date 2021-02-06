import os
from django.contrib.gis.utils import LayerMapping
from .models import pantanov_centroids

# Auto-generated `LayerMapping` dictionary for pantanov_centroids model
pantanov_centroids_mapping = {
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
    'irr_mm': 'IRR_MM',
    'geom': 'MULTIPOINT',
}

pantanov_centroids_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Shapes+end/Pantano_PumpStation/Pantano_PumpStation_Centroids.shp'))

def run(verbose=True):
    lm= LayerMapping(pantanov_centroids, pantanov_centroids_shp, pantanov_centroids_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)