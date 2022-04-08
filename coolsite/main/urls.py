from .views import *
from django.urls import path
urlpatterns=[
    path('', index, name='home'),
    path('', index, name='dko'),
    path('', index, name='prodaji'),
    path('', index, name='snab'),
]

handler404=pageNotFound