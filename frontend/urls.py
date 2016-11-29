__author__ = 'priyanktrivedi'
from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.home),
    url(r'^design/$', views.design),
    url(r'^data/$', views.data),
    url(r'^instructions/$', views.instructions),
    url(r'^terminology/$', views.terminology),
    url(r'^design_methods/$', views.design_methods),
    url(r'^next_step/$', views.next_step),
    url(r'^definitions_info/$', views.definitions_info),
    url(r'^contribute/$', views.contribute),
]
