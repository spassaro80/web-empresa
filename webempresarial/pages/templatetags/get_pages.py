from django import template 
from pages.models import Pages

register=template.Library()

@register.simple_tag
def getPages():
    pageList= Pages.objects.all()
    return pageList



