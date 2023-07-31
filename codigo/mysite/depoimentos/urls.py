from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('depoimento/criar', views.criar_depoimento, name='criar_depoimento'),
    path('depoimento/<int:id>/excluir/', views.deletar_depoimento, name='deletar_depoimento'),
]

