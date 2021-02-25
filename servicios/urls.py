from django.urls import path

from . import views

app_name = 'servicios'

urlpatterns = [
	path('', views.index, name='index'),
	path('repuesto/<int:repuesto_id>/', views.obtener_repuesto, name='obtener_repuesto'),
	path('suministro/<int:suministro_id>/', views.obtener_suministro, name='obtener_suministro'),
]