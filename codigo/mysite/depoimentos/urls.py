from django.urls import path
from . import views

urlpatterns = [
    path('criar_depoimento/', views.criar_depoimento, name='criar_depoimento'),
    path('', views.home, name='home'),
    path('depoimento/<int:depoimento_id>/excluir/', views.deletar_depoimento, name='deletar_depoimento'),
    path('depoimentos/<int:id>/editar/', views.editar_depoimento, name='editar_depoimento'),
]

