from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings 
from blog import urls
from user_auth import urls
from .views import *

urlpatterns = [
    path('login/', user_login, name='auth'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
