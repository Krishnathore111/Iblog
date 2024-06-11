
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings 
from blog import urls
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('post/<slug:url>', get_post, name="post"),
    path('category/<slug:url>', get_category, name="category"), 
    path('about/', about, name="about")
  

 
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
