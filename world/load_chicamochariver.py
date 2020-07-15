import os
from django.contrib.gis.utils import LayerMapping
from .models import chicamocha_river

# Auto-generated `LayerMapping` dictionary for chicamocha_river model
chicamocha_river_mapping = {
    'id': 'Id',
    'name': 'Name',
    'status': 'Status',
    'length': 'Length',
    'flow': 'Flow',
    'geom': 'MULTILINESTRING',
}




chicamocha_river_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'/home/marla/Documentos/shapefiles/Polygon_layers_WGS84-20200625T231731Z-001/Polygon_layers_WGS84/Chicamocha_River/Chicamocha_River.shp'))

def run(verbose=True):
    lm= LayerMapping(chicamocha_river, chicamocha_river_shp, chicamocha_river_mapping, transform=False, encoding='iso-8859-1') #transform=False,
    lm.save(strict=True, verbose=verbose)