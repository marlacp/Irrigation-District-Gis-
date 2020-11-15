from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.serializers import serialize
from .models import Countries, Incidences, Duitama_Pump, DistrictP, Ayalas_Pump, Cuche_Pump, Holanda_Pump, Lasvueltas_Pump, ministerio_Pump, moniquira_Pump, pantanov_pump, sanrafael_pump, surba_pump, tibasosa_pump, ayalas_centroides, cuche_centroides, duitama_centroides, holanda_centroids, lasvueltas_centroids, ministerio_centroids, moniquira_centroids, pantanov_centroids, sanrafael_centroids, surba_centroids, tibasosa_centroids, chicamocha_river, reservoirs

###
#a) 
#def index(request):
#    return HttpResponse("Hello, world. You're at the geodjango_Leaflet project.")


class HomePageView(TemplateView):
     template_name='world/optionMaps.html'

def clay(request):
	 return render(request, 'world/clay.html')

def slit(request):
      return render(request, 'world/slit.html')

def sand(request):
      return render(request, 'world/sand.html')

def fc(request):
      return render(request, 'world/fc.html')

def pwp(request):
      return render(request, 'world/pwp.html')

def optionMaps(request):
      return render(request, 'optionMaps.html')

def country_datasets(request):
     countries= serialize('geojson', Countries.objects.all())
     return HttpResponse(countries,content_type='json')

def incidence_points(request):
     incidences= serialize('geojson', Incidences.objects.all())
     return HttpResponse(incidences,content_type='json')     


def DuitamaPump_datasets(request):
     DuitamaPump= serialize('geojson', Duitama_Pump.objects.all())
     return HttpResponse(DuitamaPump,content_type='json') 

def DistrictPolygons_datasets(request):
     DistrictPolygons= serialize('geojson', DistrictP.objects.all())
     return HttpResponse(DistrictPolygons,content_type='json') 

def AyalasPump_datasets(request):
     AyalasPump= serialize('geojson', Ayalas_Pump.objects.all())
     return HttpResponse(AyalasPump,content_type='json') 

def Cuche_Pump_datasets(request):
     CuchePump= serialize('geojson', Cuche_Pump.objects.all())
     return HttpResponse(CuchePump,content_type='json') 

def Holanda_Pump_datasets(request):
     holandaPump= serialize('geojson', Holanda_Pump.objects.all())
     return HttpResponse(holandaPump,content_type='json') 

def Lasvueltas_Pump_datasets(request):
     lasvueltasPump= serialize('geojson', Lasvueltas_Pump.objects.all())
     return HttpResponse(lasvueltasPump,content_type='json') 

def ministerio_Pump_datasets(request):
     ministerioPump= serialize('geojson', ministerio_Pump.objects.all())
     return HttpResponse(ministerioPump,content_type='json') 

def moniquira_Pump_datasets(request):
     moniquiraPump= serialize('geojson', moniquira_Pump.objects.all())
     return HttpResponse(moniquiraPump,content_type='json') 

def pantanov_pump_datasets(request):
     pantanovpump= serialize('geojson', pantanov_pump.objects.all())
     return HttpResponse(pantanovpump,content_type='json')

def sanrafael_pump_datasets(request):
     sanrafaelpump= serialize('geojson', sanrafael_pump.objects.all())
     return HttpResponse(sanrafaelpump,content_type='json')  

def surba_pump_datasets(request):
     surbapump= serialize('geojson', surba_pump.objects.all())
     return HttpResponse(surbapump,content_type='json') 

def tibasosa_pumpdatasets(request):
     tibasosapump= serialize('geojson', tibasosa_pump.objects.all())
     return HttpResponse(tibasosapump,content_type='json') 

def ayalas_centroidesdatasets(request):
     ayalascentroides= serialize('geojson', ayalas_centroides.objects.all())
     return HttpResponse(ayalascentroides,content_type='json') 

def cuche_centroidesdatasets(request):
     cuchecentroides= serialize('geojson', cuche_centroides.objects.all())
     return HttpResponse(cuchecentroides,content_type='json') 

def duitama_centroidesdatasets(request):
     duitamacentroides= serialize('geojson', duitama_centroides.objects.all())
     return HttpResponse(duitamacentroides,content_type='json') 

def holanda_centroidsdatasets(request):
     holandacentroids= serialize('geojson', holanda_centroids.objects.all())
     return HttpResponse(holandacentroids,content_type='json') 

def lasvueltas_centroidsdatasets(request):
     lasvueltascentroids= serialize('geojson', lasvueltas_centroids.objects.all())
     return HttpResponse(lasvueltascentroids,content_type='json') 

def ministerio_centroidsdatasets(request):
     ministeriocentroids= serialize('geojson', ministerio_centroids.objects.all())
     return HttpResponse(ministeriocentroids,content_type='json') 

def moniquira_centroidsdatasets(request):
     moniquiracentroids= serialize('geojson', moniquira_centroids.objects.all())
     return HttpResponse(moniquiracentroids,content_type='json') 

def pantanov_centroidsdatasets(request):
     pantanovcentroids= serialize('geojson', pantanov_centroids.objects.all())
     return HttpResponse(pantanovcentroids,content_type='json') 

def sanrafael_centroidsdatasets(request):
     sanrafaelcentroids= serialize('geojson', sanrafael_centroids.objects.all())
     return HttpResponse(sanrafaelcentroids,content_type='json') 

def surba_centroidsdatasets(request):
     surbacentroids= serialize('geojson', surba_centroids.objects.all())
     return HttpResponse(surbacentroids,content_type='json') 

def tibasosa_centroidsdatasets(request):
     tibasosacentroids= serialize('geojson', tibasosa_centroids.objects.all())
     return HttpResponse(tibasosacentroids,content_type='json') 

def chicamocha_riverdatasets(request):
     chicamochariver= serialize('geojson', chicamocha_river.objects.all())
     return HttpResponse(chicamochariver,content_type='json') 

def reservoirs_datasets(request):
     reservoirsdata= serialize('geojson', reservoirs.objects.all())
     return HttpResponse(reservoirsdata,content_type='json') 