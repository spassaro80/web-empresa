from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Pages(models.Model):
    title = models.CharField(max_length=200, verbose_name=("Título"))
    text = RichTextField(verbose_name="Contexto")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    class Meta:
        verbose_name = 'Página generica'
        verbose_name_plural = 'Páginas genéricas'
        ordering = ['order','title']
    def __str__(self):
        return self.title
