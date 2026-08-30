from django.urls import path
from . import views

urlpatterns = [
    path("openf1/pilotos/", views.pilotos_openf1, name="pilotos_openf1")
]