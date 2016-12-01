__author__ = 'priyaltrivedi'
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
    url(r'^indicators_info/$', views.indicators_info),
    url(r'^methods_info/$', views.methods_info),
    url(r'^indicators_list/$', views.indicators_list),
    url(r'^fetch_lc_phase/$', views.fetch_lc_phase),
    url(r'^contribute/$', views.contribute),
]
