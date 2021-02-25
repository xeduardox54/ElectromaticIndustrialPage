from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.
def index(request):
    lastredes = redes.objects.last()
    lastvideo = video.objects.last()
    mantenimiento_object = mantenimiento.objects.last()
    instalacion_object = instalacion.objects.last()
    repuesto_object = repuesto.objects.last()
    suministro_object = suministro.objects.last()
    contacto_object = contacto.objects.last()
    try:
    	video_presentacion = lastvideo.video_presentacion
    except:
    	video_presentacion = None
    context = {
    	'video_presentacion' : video_presentacion,
        'redes' : lastredes,
        'mantenimiento' : mantenimiento_object,
        'instalacion' : instalacion_object,
        'repuestos': repuesto_object,
        'suministro': suministro_object,
        'contactos': contacto_object,
    }
    return render(request,'contactos.html', context)

def obtener_repuesto(request, repuesto_id):
    repuesto_object = get_object_or_404(repuestos_articulos, pk=repuesto_id)
    repuesto_list = repuesto.objects.last()
    articulos_list = repuesto_list.articulos.exclude(pk=repuesto_id)
    context = {
        'repuesto' : repuesto_object,
        'repuestos' : articulos_list,
    }
    return render(request,'repuesto.html',context)

def obtener_suministro(request, suministro_id):
    suministro_object = get_object_or_404(suministros_articulos, pk=suministro_id)
    suministro_list = suministro.objects.last()
    articulos_list = suministro_list.articulos.exclude(pk=suministro_id)
    context = {
        'suministro' : suministro_object,
        'suministros' : articulos_list,
    }
    return render(request,'suministro.html',context)