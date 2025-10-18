from django .urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal),
    path('categoria/', views.pagina_categoria),
    path('detalle/', views.pagina_detalle),
]
