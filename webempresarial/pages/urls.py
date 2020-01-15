from django.urls import path
from . import views 
    
urlpatterns = [
    path('<int:page_id>/<slug:page_name>/', views.pages, name="pages" ),
]