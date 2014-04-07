airotub
=======

Youtube Downloader django app

Website Aaron Diaz R (dev) : www.ironsistem.com

Pafy (python youtube lib) : http://np1.github.io/pafy/


Instrucciones de instalacion:
==============================

    1.- Agregar al settings.py la aplicacion 'apps.airotub'
    2.- Agregar a su archivo de urls.py del proyecto:
         url(r'^airotub/', include('apps.airotub.urls', namespace="airotub"))
    3.- Agrega los archivos estaticos y de template al proyecto donde seas instalar la app
    4.- Tener configurada la variable STATIC_URL
    5.- Cumplir con las siguientes dependencias:
          Django==1.6.2
          Unipath==1.0
          argparse==1.2.1
          wsgiref==0.1.2
    



          
          


