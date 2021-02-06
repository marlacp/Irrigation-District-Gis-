import os
from django.contrib.gis.utils import LayerMapping
from .models import sanrafael_pump

# Auto-generated `LayerMapping` dictionary for sanrafael_pump model
sanrafael_pump_mapping = {
    'id': 'ID',
    'code': 'CODE',
    'lon': 'LON',
    'lat': 'LAT',
    'area': 'AREA',
    'clay': 'CLAY',
    'silt': 'SILT',
    'sand': 'SAND',
    'fc': 'FC',
    'pwp': 'PWP',
    'ks': 'KS',
    'prescriptio': 'PRESCRIPTIO',
    'crop_n': 'CROP_N',
    'crop_c': 'CROP_C',
    'irr_mm': 'IRR_MM',
    'geom': 'MULTIPOLYGON',
}


sanrafael_pump_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Shapes+end/SanRafael_PumpStation/SanRafael_PumpStation_Polygon.shp'))

def run(verbose=True):
    lm= LayerMapping(sanrafael_pump, sanrafael_pump_shp, sanrafael_pump_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)