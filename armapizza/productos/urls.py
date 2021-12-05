from django.contrib import admin
from django.urls import path

from . import views

app_name = "productos_app"

urlpatterns = [

    path('api/quesos/list',views.QuesosListAPIView.as_view(),name="quesosapi"),
    path('api/masas/list',views.MasaListAPIView.as_view(),name="masasapi"),
    path('api/tiposingredientes/list',views.TipoIngredienteListAPIView.as_view(),name="tiposingredientesapi"),
    path('api/ingredientes/list',views.IngredienteListAPIView.as_view(),name="ingredientesapi"),
    path('api/otrosproductos/list',views.OtroProductoListAPIView.as_view(),name="otrosproductosapi"),
    path('api/menutradicional/list',views.MenuTradicionalListAPIView.as_view(),name="menutradicionalapi"),

]
