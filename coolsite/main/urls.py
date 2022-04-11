from .views import *
from django.urls import path
urlpatterns=[
    path('', index, name='home'),
    path('/dko', index_dko, name='dko'),
    path('/prodaji', index_prodaji, name='prodaji'),
    path('/snab', index_snab, name='snab'),
]

handler404=pageNotFound