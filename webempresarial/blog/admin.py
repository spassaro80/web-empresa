from django.contrib import admin
from .models import Category,Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','modified')

admin.site.register(Category,CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','modified')
    list_display=('title','text','published','post_categories')
    ordering=('title', 'published')
    search_fields=('title','text','user__username','category__title')
    date_hierarchy=('published')
    list_filter=('user__username','category__title')
    def post_categories(self,obj):
        return(", ".join([c.title for c in obj.category.all()]))
    post_categories.short_description = "Categorías"

admin.site.register(Post,PostAdmin)




