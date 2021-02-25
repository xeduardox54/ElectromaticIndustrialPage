from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(video)
admin.site.register(redes)
admin.site.register(mantenimiento)
admin.site.register(instalacion)
admin.site.register(repuesto)
admin.site.register(suministro)
admin.site.register(contacto)
admin.site.register(mantenimientos_imagenes)
admin.site.register(instalaciones_imagenes)
admin.site.register(repuestos_articulos)
admin.site.register(suministros_articulos)
admin.site.register(contactos_clientes)