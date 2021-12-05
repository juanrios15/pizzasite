from django.contrib import admin
from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [

    path('api/portadas/list',views.PortadaListAPIView.as_view(),name="portadasapi"),

]