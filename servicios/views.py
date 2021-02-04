from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    lastvideo = video.objects.last()
    try:
    	video_presentacion = lastvideo.video_presentacion
    except:
    	video_presentacion = None
    context = {
    	'video_presentacion' : video_presentacion,
    }
    return render(request,'index.html', context)