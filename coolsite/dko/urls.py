from .views import *
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('', MainDko.as_view(), name='main_dko'),
    path('show_eq/<slug:client_slug>', ShowEquipment.as_view(), name='dko_show_eq'),
    # path('show_eq', ShowEquipment.as_view(), name='dko_show_eq'),
    # path('show_eq', AddEquipment.as_view(), name='dko_show_eq'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
