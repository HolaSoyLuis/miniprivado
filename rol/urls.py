from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import vistaRegistro, listaRegistro, editarRegistro, eliminarRegistro
from .views import create_empleado, empleado_list
from .views import create_afiliado, afiliado_list
from .views import principal

urlpatterns = [
    path('', principal, name = 'principal'),
    path('registro', vistaRegistro.as_view(), name = 'registro'),
    path('listaRegistro', listaRegistro.as_view(), name = 'listaRegistro'),
    path('editarRegistro/(?P<pk>\d+)/', editarRegistro.as_view(), name = 'editarRegistro'),
    path('eliminarRegistro/(?P<pk>\d+)/$', eliminarRegistro.as_view(), name = 'eliminarRegistro'),
    #empleado
    path('create_empleado', create_empleado, name = 'create_empleado'),
    path('empleado_list', empleado_list, name = 'empleado_list'),
    #afiliado
    path('create_afiliado', create_afiliado, name = 'create_afiliado'),
    path('afiliado_list', afiliado_list, name = 'afiliado_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

