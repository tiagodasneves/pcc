from django.urls import path
from . import views

urlpatterns = [
    path('criar_depoimento/', views.criar_depoimento, name='criar_depoimento'),
    path('depoimentos/', views.depoimentos, name='depoimentos'),
    path('depoimento/<int:depoimento_id>/excluir/', views.deletar_depoimento, name='deletar_depoimento'),
]
