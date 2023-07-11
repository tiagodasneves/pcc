from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.sair, name='logout'),
    path('ler_usuarios/', views.ler_usuarios, name='ler_usuarios'),
    path('editar_usuario/<int:id>', views.editar_usuario, name='editar_usuario'),
    path('deletar_usuario/<int:id>', views.deletar_usuario, name='deletar_usuario'),
    path('editar_perfil/<int:id>', views.editar_perfil, name='editar_perfil'),
]
