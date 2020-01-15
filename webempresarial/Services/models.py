from django.db import models

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name=("Título"))
    subtitle = models.CharField(max_length=200, verbose_name=("Subtitulo"))
    context = models.TextField(verbose_name="Contexto")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-created']
    def __str__(self):
        return self.title

