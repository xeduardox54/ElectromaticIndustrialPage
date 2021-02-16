from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    lastvideo = video.objects.last()
    mantenimiento_imagenes = mantenimiento.objects.all()
    instalacion_imagenes = instalacion.objects.all()
    repuesto_imagenes = repuesto.objects.all()
    try:
    	video_presentacion = lastvideo.video_presentacion
    except:
    	video_presentacion = None
    context = {
    	'video_presentacion' : video_presentacion,
        'mantenimiento_imagenes' : mantenimiento_imagenes,
        'instalacion_imagenes' : instalacion_imagenes,
        'repuesto_imagenes': repuesto_imagenes,
    }
    return render(request,'scripts.html', context)