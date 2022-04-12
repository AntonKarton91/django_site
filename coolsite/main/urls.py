from .views import *
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('', index, name='home'),
    path('blog', show_blog, name='blogs'),
    path('dko', index_dko, name='dko'),
    path('prodaji', index_prodaji, name='prodaji'),
    path('snab', index_snab, name='snab'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

