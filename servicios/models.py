from django.db import models

# Create your models here.
class video(models.Model):
	video_presentacion = models.FileField(upload_to='videos/', null=True, verbose_name="")