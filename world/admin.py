from django.contrib import admin
#from django.contrib.gis.admin import OSMGeoAdmin
from .models import Incidences, Countries, Duitama_Pump, DistrictP, Ayalas_Pump ,Cuche_Pump, Holanda_Pump, Lasvueltas_Pump, ministerio_Pump, moniquira_Pump, pantanov_pump, sanrafael_pump, surba_pump, tibasosa_pump, ayalas_centroides, cuche_centroides, duitama_centroides, holanda_centroids, lasvueltas_centroids, ministerio_centroids, moniquira_centroids, pantanov_centroids, sanrafael_centroids, surba_centroids, tibasosa_centroids
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

#@admin.register(Incidences)
class IncidencesAdmin(LeafletGeoAdmin):
	list_display =('name','location')
	#pass

class CountriesAdmin(LeafletGeoAdmin):
	list_display =('name','region')
	#pass

class DistrictPAdmin(LeafletGeoAdmin):
	list_display =('name','geom')
	#pass

class Duitama_PumpAdmin(LeafletGeoAdmin):
	list_display =('code','geom')

class Ayalas_PumpAdmin(LeafletGeoAdmin):
	list_display =('code','geom')

class Cuche_PumpAdmin(LeafletGeoAdmin):
	list_display =('code','geom')

class Holanda_PumpAdmin(LeafletGeoAdmin):
	list_display =('code','geom')

class Lasvueltas_PumpAdmin(LeafletGeoAdmin):
	list_display =('code','geom')

class ministerio_PumpAdmin(LeafletGeoAdmin):
	list_display =('code','geom')

class moniquira_PumpAdmin(LeafletGeoAdmin):
	list_display =('code','geom')

class pantanov_pumpAdmin(LeafletGeoAdmin):
	list_display =('code','geom')

class sanrafael_pumpAdmin(LeafletGeoAdmin):
	list_display =('code','geom')

class surba_pumpAdmin(LeafletGeoAdmin):
	list_display =('code','geom')

class tibasosa_pumpAdmin(LeafletGeoAdmin):
	list_display =('code','geom')

class ayalas_centroidesAdmin(LeafletGeoAdmin):
	list_display =('code','geom')

class cuche_centroidesAdmin(LeafletGeoAdmin):
	list_display =('code','geom')

class duitama_centroidesAdmin(LeafletGeoAdmin):
	list_display =('code','geom')


class holanda_centroidsAdmin(LeafletGeoAdmin):
	list_display =('code','geom')


class lasvueltas_centroidsAdmin(LeafletGeoAdmin):
	list_display =('code','geom')


class ministerio_centroidsAdmin(LeafletGeoAdmin):
	list_display =('code','geom')

class moniquira_centroidsAdmin(LeafletGeoAdmin):
	list_display =('code','geom')


class pantanov_centroidsAdmin(LeafletGeoAdmin):
	list_display =('code','geom')


class sanrafael_centroidsAdmin(LeafletGeoAdmin):
	list_display =('code','geom')


class surba_centroidsAdmin(LeafletGeoAdmin):
	list_display =('code','geom')


class tibasosa_centroidsAdmin(LeafletGeoAdmin):
	list_display =('code','geom')


admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Countries, CountriesAdmin)
admin.site.register(DistrictP, DistrictPAdmin)
admin.site.register(Duitama_Pump, Duitama_PumpAdmin)
admin.site.register(Ayalas_Pump, Ayalas_PumpAdmin)
admin.site.register(Cuche_Pump, Cuche_PumpAdmin)
admin.site.register(Holanda_Pump, Holanda_PumpAdmin)
admin.site.register(Lasvueltas_Pump, Lasvueltas_PumpAdmin)
admin.site.register(ministerio_Pump, ministerio_PumpAdmin)
admin.site.register(moniquira_Pump, moniquira_PumpAdmin)
admin.site.register(pantanov_pump, pantanov_pumpAdmin)
admin.site.register(sanrafael_pump, sanrafael_pumpAdmin)
admin.site.register(surba_pump, surba_pumpAdmin)
admin.site.register(tibasosa_pump, tibasosa_pumpAdmin)
admin.site.register(ayalas_centroides, ayalas_centroidesAdmin)
admin.site.register(duitama_centroides, duitama_centroidesAdmin)
admin.site.register(holanda_centroids, holanda_centroidsAdmin)
admin.site.register(lasvueltas_centroids, lasvueltas_centroidsAdmin)
admin.site.register(ministerio_centroids, ministerio_centroidsAdmin)
admin.site.register(moniquira_centroids, moniquira_centroidsAdmin)
admin.site.register(pantanov_centroids, pantanov_centroidsAdmin)
admin.site.register(sanrafael_centroids, sanrafael_centroidsAdmin)
admin.site.register(surba_centroids, surba_centroidsAdmin)
admin.site.register(tibasosa_centroids, tibasosa_centroidsAdmin)