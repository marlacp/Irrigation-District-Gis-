from django.conf.urls import url, include
from .views import HomePageView, ContactPageView
from django.urls import path
###

#a) 
#urlpatterns = [
#    path('world/', include('world.urls')),
#    path('admin/', admin.site.urls),
#]

urlpatterns = [
   # url(r'^', include('home.urls'))
   url(r'^$', HomePageView.as_view(), name='home'),
   url(r'^contact/$', ContactPageView.as_view(), name='contact'),
] 