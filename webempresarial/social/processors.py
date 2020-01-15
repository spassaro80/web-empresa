from .models import Link

def context(render):
    sociallinks = {}
    links = Link.objects.all()
    for link in links:
        sociallinks[link.title] = link.url  
    return sociallinks