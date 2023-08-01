from django.urls import path
from . import views

urlpatterns = [
    path('peruca/cadastrar', views.cadastrar_peruca, name='cadastrar_peruca'),
    path('peruca/listar', views.listar_perucas, name='listar_perucas'),
    path('peruca/<int:id>/editar/', views.editar_peruca, name='editar_peruca'),
    path('peruca/<int:id>/deletar/', views.deletar_peruca, name='excluir_peruca'),
    path('minhas_solicitacoes/', views.minhas_solicitacoes, name='minhas_solicitacoes'),
    path('fazer_solicitacao/', views.fazer_solicitacao, name='fazer_solicitacao'),
    path('solicitacao/listar', views.listar_solicitacoes, name='listar_solicitacoes'),
    path('solicitacao/<int:id>/', views.detalhes_solicitacao, name='detalhes_solicitacao'),
    path('solicitacao/<int:id>/aprovar/', views.aprovar_solicitacao, name='aprovar_solicitacao'),
    path('solicitacao/<int:id>/rejeitar/', views.rejeitar_solicitacao, name='rejeitar_solicitacao'),
    path('solicitacao/<int:id>/addCR/', views.addCR, name='addCR'),
    path('solicitacao/<int:id>/finalizar_entrega/', views.finalizar_entrega, name='finalizar_entrega'),
    path('solicitacao/<int:id>/deletar', views.deletar_solicitacao, name="deletar_solicitacao")
] 