from django.contrib import admin
from django.urls import path

from . import views

app_name = "pedidos_app"

urlpatterns = [

    path('api/tamanos/list',views.TamanosListAPIView.as_view(),name="tamanosapi"),
    path('api/pedidos/create',views.PedidoCreateAPIView.as_view(),name="pedidosapi"),
    path('api/pizza/create',views.PizzaCreateAPIView.as_view(),name="pizzaspi"),
    path('api/ingredientes/create',views.IngredientesPizzaCreateAPIView.as_view(),name="ingredientesapi"),
    path('api/otros/create',views.OtrosCreateAPIView.as_view(),name="otrosapi"),

]
