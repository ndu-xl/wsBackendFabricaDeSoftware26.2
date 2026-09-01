"""
URL configuration for projetoFabricaDeSoftware project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from f1_manage.api import viewsets
from rest_framework import routers
from f1_manage import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

route = routers.DefaultRouter()


route.register(r'pilotos', viewsets.PilotoViewSet, basename="Piloto")
route.register(r'equipe', viewsets.EquipeViewSet, basename="Equipe")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path("openf1/pilotos/",views.pilotos_openf1),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('swagger/',SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]
