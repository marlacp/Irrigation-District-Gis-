from django.conf.urls import include, url
from .views import HomePageView, ayalas_centroidesdatasets, AyalasPump_datasets,cuche_centroidesdatasets, Cuche_Pump_datasets, duitama_centroidesdatasets, DuitamaPump_datasets, holanda_centroidsdatasets, Holanda_Pump_datasets, lasvueltas_centroidsdatasets, Lasvueltas_Pump_datasets, ministerio_centroidsdatasets, ministerio_Pump_datasets, moniquira_centroidsdatasets, moniquira_Pump_datasets, pantanov_centroidsdatasets, pantanov_pump_datasets,sanrafael_centroidsdatasets, sanrafael_pump_datasets, surba_centroidsdatasets, surba_pump_datasets,  tibasosa_centroidsdatasets, tibasosa_pumpdatasets,  DistrictPolygons_datasets,  country_datasets, incidence_points, chicamocha_riverdatasets, reservoirs_datasets
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
#   
###      

#a) 

#urlpatterns = [
#    path('', views.index, name='index'),
#]


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^country_data/$', country_datasets, name='country'),
    url(r'^incidence_data/$', incidence_points, name='incidences'),
    url(r'^district_data/$', DistrictPolygons_datasets, name='District'),
    url(r'^duitamapump_data/$', DuitamaPump_datasets, name='DuitamaPump'),
    url(r'^ayalaspump_data/$', AyalasPump_datasets, name='AyalasPump'),
    url(r'^cuchepump_data/$', Cuche_Pump_datasets, name='CuchePump'),
    url(r'^holandapump_data/$', Holanda_Pump_datasets, name='HolandaPump'),
    url(r'^lasvueltas_data/$', Lasvueltas_Pump_datasets, name='lasvueltasPump'),
    url(r'^ministerio_data/$', ministerio_Pump_datasets, name='ministerioPump'),
    url(r'^moniquira_data/$', moniquira_Pump_datasets, name='moniquiraPump'),
    url(r'^pantanov_data/$', pantanov_pump_datasets, name='pantanovPump'),
    url(r'^sanrafael_data/$', sanrafael_pump_datasets, name='sanrafaelpump'),
    url(r'^surbapump_data/$', surba_pump_datasets, name='surbapump'),
    url(r'^tibasosapump_data/$', tibasosa_pumpdatasets, name='tibasosapump'),
    url(r'^ayalascentroides_data/$', ayalas_centroidesdatasets, name='ayalascentroides'),
    url(r'^cuchecentroides_data/$', cuche_centroidesdatasets, name='cuchecentroides'),
    url(r'^duitamacentroides_data/$', duitama_centroidesdatasets, name='duitamacentroides'),
    url(r'^holandacentroids_data/$', holanda_centroidsdatasets, name='holandacentroids'),
    url(r'^lasvueltas_centroids/$', lasvueltas_centroidsdatasets, name='lasvueltascentroids'),
    url(r'^ministerio_centroids/$', ministerio_centroidsdatasets, name='ministeriocentroids'),
    url(r'^moniquira_centroids/$', moniquira_centroidsdatasets, name='moniquiracentroids'),
    url(r'^pantanov_centroids/$', pantanov_centroidsdatasets, name='pantanovcentroids'),
    url(r'^sanrafael_centroids/$', sanrafael_centroidsdatasets, name='sanrafaelcentroids'),
    url(r'^tibasosa_centroids/$', tibasosa_centroidsdatasets, name='tibasosacentroids'),
    url(r'^surba_centroids/$', surba_centroidsdatasets, name='surbacentroids'),
    url(r'^chicamocha_river/$', chicamocha_riverdatasets, name='chicamochariver'),
    url(r'^reservoirs/$', reservoirs_datasets, name='reservoirs'),
    path('clay/', views.clay, name='clay'),
    path('silt/', views.slit, name='slit'),
    path('sand/', views.sand, name='sand'),
    path('fc/', views.fc, name='fc'),
    path('pwp/', views.pwp, name='pwp'),
    path('ks/', views.ks, name='ks'),
    path('crop/', views.crop, name='crop'),
    path('prescription/', views.prescription, name='prescription'),
    path('optionMaps/', views.optionMaps, name='optionMaps')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

