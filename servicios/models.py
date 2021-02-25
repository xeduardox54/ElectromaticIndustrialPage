from django.db import models

class video(models.Model):
	video_presentacion = models.FileField(upload_to='videos/', null=True, verbose_name="Vídeo de presentación")

	def __str__(self):
		return "Vídeo de presentación"

class redes(models.Model):
	youtube = models.CharField(max_length=500)
	facebook = models.CharField(max_length=500)
	twitter = models.CharField(max_length=500)
	linkedin = models.CharField(max_length=500)

	def __str__(self):
		return "Redes sociales"

#Sección mantenimiento
class mantenimientos_imagenes(models.Model):
	imagen = models.ImageField(upload_to='mantenimiento/',blank=True,null=True)

	def __str__(self):
		return "Imagen " + str(self.pk)	

class mantenimiento(models.Model):
	servicio_imagen = models.ImageField(upload_to='mantenimiento/',blank=True,null=True)
	portada_imagen = models.ImageField(upload_to='mantenimiento/',blank=True,null=True)
	contenido = models.TextField()
	portada_preventivo = models.ImageField(upload_to='mantenimiento/',blank=True,null=True)
	contenido_preventivo = models.TextField()
	portada_correctivo = models.ImageField(upload_to='mantenimiento/',blank=True,null=True)
	contenido_correctivo = models.TextField()
	imagenes = models.ManyToManyField(mantenimientos_imagenes)

	def __str__(self):
		return "Sección mantenimiento"

#Sección instalación
class instalaciones_imagenes(models.Model):
	imagen = models.ImageField(upload_to='instalacion/',blank=True,null=True)
	
	def __str__(self):
		return "Imagen " + str(self.pk)

class instalacion(models.Model):
	servicio_imagen = models.ImageField(upload_to='instalacion/',blank=True,null=True)
	portada_imagen = models.ImageField(upload_to='instalacion/',blank=True,null=True)
	contenido = models.TextField()
	imagenes = models.ManyToManyField(instalaciones_imagenes)

	def __str__(self):
		return "Sección instalación"

#Sección repuesto
class repuestos_articulos(models.Model):
	nombre = models.CharField(max_length=500)
	descripcion = models.TextField()
	precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
	precio_alquiler = models.DecimalField(max_digits=10, decimal_places=2)
	imagen = models.ImageField(upload_to='repuestos/',blank=True,null=True)

	def __str__(self):
		return self.nombre

class repuesto(models.Model):
	servicio_imagen = models.ImageField(upload_to='repuestos/',blank=True,null=True)
	portada_imagen = models.ImageField(upload_to='repuestos/',blank=True,null=True)
	contenido = models.TextField()
	articulos = models.ManyToManyField(repuestos_articulos)

	def __str__(self):
		return "Sección Repuesto"

#Sección suministros
class suministros_articulos(models.Model):
	nombre = models.CharField(max_length=500)
	descripcion = models.TextField()
	precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
	precio_alquiler = models.DecimalField(max_digits=10, decimal_places=2)
	imagen = models.ImageField(upload_to='suministros/',blank=True,null=True)

	def __str__(self):
		return self.nombre

class suministro(models.Model):
	servicio_imagen = models.ImageField(upload_to='suministros/',blank=True,null=True)
	portada_imagen = models.ImageField(upload_to='suministros/',blank=True,null=True)
	contenido = models.TextField()
	articulos = models.ManyToManyField(suministros_articulos)

	def __str__(self):
		return "Sección suministros"

#Sección contactos
class contactos_clientes(models.Model):
	empresa_imagen = models.ImageField(upload_to='contactos/',blank=True,null=True)

	def __str__(self):
		return "Imagen " + str(self.pk)

class contacto(models.Model):
	direccion = models.CharField(max_length=500)
	telefono = models.CharField(max_length=100)
	correo = models.EmailField(max_length=200)
	sitio_web = models.CharField(max_length=200)
	clientes = models.ManyToManyField(contactos_clientes)

	def __str__(self):
		return "Sección contactos"