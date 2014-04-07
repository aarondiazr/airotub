from django.conf.urls import patterns, include, url
#from .views import *

urlpatterns = patterns('apps.airotub.views',
	url(r'^$', 'index'),
	url(r'^getinf/(.*?)$', 'GetInfo'),
	url(r'^getdown/(.*?)/(\d+)$', 'GetStream'),
	url(r'^prueba/$', 'Prueba'),
)
