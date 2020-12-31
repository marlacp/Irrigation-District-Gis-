import os
from django.contrib.gis.utils import LayerMapping
from .models import cuche_centroides

# Auto-generated `LayerMapping` dictionary for cuche_centroides model
cuche_centroides_mapping = {
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


cuche_centroides_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/ShapeFinales/shp_PmS/Cuche_PumpStation/Cuche_PumpStation_Centroids.shp'))

def run(verbose=True):
    lm= LayerMapping(cuche_centroides, cuche_centroides_shp, cuche_centroides_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)