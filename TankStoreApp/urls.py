from django .urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='principal'),
    path('categoria/<int:categoria_id>/', views.pagina_categoria, name='categoria'),
    path('detalle/<int:tanque_id>/', views.pagina_detalle, name='detalle'),
]