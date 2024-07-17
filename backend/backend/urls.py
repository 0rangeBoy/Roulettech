"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from personalApp import views

routerText = routers.DefaultRouter()
routerText.register(r'pApp', views.PersonalAppViewText, 'personalAppText')

routerImg = routers.DefaultRouter()
routerImg.register(r'pApp', views.PersonalAppViewIMG, 'personalAppIMG')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('apiText/', include(routerText.urls)),
    path('apiImg/', include(routerImg.urls)),
]
