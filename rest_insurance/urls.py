from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static

from rest_insurance import views

urlpatterns = [

    url(r'^homepage/', views.homepage,name='homepage'),
    url(r'^login/',views.login,name='login'),
    ]
