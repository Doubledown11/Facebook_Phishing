from django.urls import path, include 
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin



app_name = 'login'

urlpatterns = [
    path('', views.home, name='home'),

]