from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name=("Categoría"))
    created = models.DateField(auto_now_add=True, verbose_name="Fecha creación")
    modified = models.DateField(auto_now=True, verbose_name="Fecha edición")
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created']
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name=("Título"))
    image = models.ImageField(verbose_name="Imagen", upload_to="category", null=True, blank=True)
    text = models.TextField(verbose_name="Entrada")
    published = models.DateField(verbose_name="Publicado el ", default=now())
    user = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, verbose_name="Categoría", related_name="get_posts")  
    created = models.DateField(auto_now_add=True, verbose_name="Fecha creación")
    modified = models.DateField(auto_now=True, verbose_name="Fecha edición")
    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']
    def __str__(self):
        return self.title

