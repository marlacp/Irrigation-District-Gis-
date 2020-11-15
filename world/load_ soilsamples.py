import os
from django.contrib.gis.utils import LayerMapping
from .models import soilsamples

# Auto-generated `LayerMapping` dictionary for soilsamples model
soilsamples_mapping = {
    'obs.': 'Obs.',
    'point': 'Point',
    'lat': 'LAT',
    'lon': 'LON',
    'pumpstatio': 'PUMPSTATIO',
    'use': 'USE',
    'clay': 'CLAY',
    'silt': 'SILT',
    'sand': 'SAND',
    'density': 'DENSITY',
    'sp': 'SP',
    'fc': 'FC',
    'pwp': 'PWP',
    'hc': 'HC',
    'geom': 'MULTIPOINT',
    
}





soilsamples_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Polygon_layers_WGS84-20200625T231731Z-001/Polygon_layers_WGS84/SoilSamplePoints/SoilSamples.shp'))

def run(verbose=True):
    lm= LayerMapping(soilsamples, soilsamples_shp, soilsamples_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)