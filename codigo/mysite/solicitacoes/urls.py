from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_peruca/', views.cadastrar_peruca, name='cadastrar_peruca'),
    path('perucas/', views.listar_perucas, name='listar_perucas'),
    path('editar_peruca/<int:pk>/', views.editar_peruca, name='editar_peruca'),
    path('excluir_peruca/<int:pk>/', views.excluir_peruca, name='excluir_peruca'),
    path('fazer_solicitacao/', views.fazer_solicitacao, name='fazer_solicitacao'),
    path('solicitacoes/', views.listar_solicitacoes, name='listar_solicitacoes'),
    path('solicitacoes/<int:solicitacao_id>/', views.detalhes_solicitacao, name='detalhes_solicitacao'),
    path('solicitacao/<int:solicitacao_id>/aprovar/', views.aprovar_solicitacao, name='aprovar_solicitacao'),
    path('solicitacao/<int:solicitacao_id>/rejeitar/', views.rejeitar_solicitacao, name='rejeitar_solicitacao'),
    path('solicitacoes/addCR/<int:solicitacao_id>/', views.addCR, name='addCR'),
    path('minhas_solicitacoes/', views.minhas_solicitacoes, name='minhas_solicitacoes'),
    path('finalizar_entrega/<int:solicitacao_id>/', views.finalizar_entrega, name='finalizar_entrega'),
] 