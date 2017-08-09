from django.conf.urls import url
from . import  views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^equipments/list/$', views.list_equipments, name='list_equipments'),
    url(r'^equipments/new/$', views.edit_equipment, name='new_equipment'),
    url(r'^equipments/edit/(?P<equipment_pk>[\d-]+)$', views.edit_equipment, name='edit_equipment'),
    url(r'^equipments/delete/(?P<equipment_pk>[\d-]+)$', views.delete_equipment, name='delete_equipment'),
    url(r'^clients/list/$', views.list_clients, name='list_clients'),
    url(r'^clients/new/$', views.edit_client, name='new_client'),
    url(r'^clients/edit/(?P<client_pk>[\d-]+)$', views.edit_client, name='edit_client'),
    url(r'^clients/delete/(?P<client_pk>[\d-]+)$', views.delete_client, name='delete_client'),
    url(r'^leasings/new/$', views.new_leasing, name='new_leasing'),
    url(r'^leasings/list/$', views.view_leasing, name='view_leasing'),
    url(r'^leasings/delete/(?P<leasing_pk>[\d-]+)$', views.delete_leasing, name='delete_leasing'),
    url(r'^mapping/map.html$', views.map, name='map')
]