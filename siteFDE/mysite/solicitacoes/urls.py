from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_peruca/', views.cadastrar_peruca, name='cadastrar_peruca'),
    path('listar_perucas/', views.listar_perucas, name='listar_perucas'),
    path('editar_peruca/<int:pk>/', views.editar_peruca, name='editar_peruca'),
    path('excluir_peruca/<int:pk>/', views.excluir_peruca, name='excluir_peruca'),
] 