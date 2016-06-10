from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^equilibration$', views.equilibration, name='equilibration'),
    url(r'^insertion$', views.insertion, name='insertion'),
    url(r'^umbrella', views.umbrella, name='umbrella'),
    url(r'^lipids', views.lipids, name='lipids'),
    url(r'^membranes', views.membranes, name='membranes'),
    url(r'^forcefields', views.forcefields, name='forcefields'),
    url(r'^jobs', views.jobs, name='jobs'),
]
