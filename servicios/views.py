from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.
def index(request):
    lastvideo = video.objects.last()
    mantenimiento_imagenes = mantenimiento.objects.all()
    instalacion_imagenes = instalacion.objects.all()
    repuestos = repuesto.objects.all()
    try:
    	video_presentacion = lastvideo.video_presentacion
    except:
    	video_presentacion = None
    context = {
    	'video_presentacion' : video_presentacion,
        'mantenimiento_imagenes' : mantenimiento_imagenes,
        'instalacion_imagenes' : instalacion_imagenes,
        'repuestos': repuestos,
    }
    return render(request,'contactos.html', context)

def obtener_repuesto(request, repuesto_id):
    repuesto_object = get_object_or_404(repuesto, pk=repuesto_id)
    repuesto_list = repuesto.objects.all()
    context = {
        'repuesto' : repuesto_object,
        'repuestos' : repuesto_list,
    }
    return render(request,'repuesto.html',context)