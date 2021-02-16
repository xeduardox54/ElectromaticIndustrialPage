from django.db import models

# Create your models here.
class video(models.Model):
	video_presentacion = models.FileField(upload_to='videos/', null=True, verbose_name="")

class mantenimiento(models.Model):
	imagen = models.ImageField(upload_to='mantenimiento/',blank=True,null=True)

class instalacion(models.Model):
	imagen = models.ImageField(upload_to='instalacion/',blank=True,null=True)

class repuesto(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=10000)
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	imagen = models.ImageField(upload_to='repuestos/',blank=True,null=True)

	def __str__(self):
		return self.nombre