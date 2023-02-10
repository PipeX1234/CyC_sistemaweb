from django.urls import path
from .views import mostrar_index, mostrar_ventajas, mostrar_trabajos, mostrar_servicios, mostrar_presupuesto, iniciar_sesion, mostrar_presupuesto_admin, cerrar_sesion

urlpatterns = [ 
    path('',mostrar_index, name="index"),
    path('ventajas',mostrar_ventajas, name="ventajas"),
    path('trabajos', mostrar_trabajos, name="trabajos"),
    path('servicios', mostrar_servicios, name="servicios"),
    path('presupuesto', mostrar_presupuesto, name="presupuesto"),
    path('iniciar_sesion', iniciar_sesion, name="iniciar_sesion"),
    path('presupuesto_admin/<action>', mostrar_presupuesto_admin, name="presupuesto_admin"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion")
]


#path("historialVenta/<id>/<action>", historialVenta, name="historialVenta"),