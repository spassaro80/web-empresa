from django.contrib import admin
from .models import Link

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','modified')

admin.site.register(Link,ProjectAdmin)
