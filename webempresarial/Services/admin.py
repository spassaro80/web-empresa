from django.contrib import admin
from .models import Services

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','modified')

admin.site.register(Services,ProjectAdmin)