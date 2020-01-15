from django.db import models

# Create your models here.

class Link(models.Model):
    title = models.SlugField(max_length=100, verbose_name="Identificador", unique=True)
    name = models.CharField(max_length=200, verbose_name=("Nombre"))
    url = models.URLField(verbose_name="Enlace", null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['-name']
    def __str__(self):
        return self.title
