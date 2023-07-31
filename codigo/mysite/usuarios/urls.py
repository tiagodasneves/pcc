from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.sair, name='logout'),
    path('usuarios/ler', views.ler_usuarios, name='ler_usuarios'),
    path('usuario/<int:id>/editar', views.editar_usuario, name='editar_usuario'),
    path('usuario/<int:id>/deletar', views.deletar_usuario, name='deletar_usuario'),
    path('perfil/<int:id>/editar', views.editar_perfil, name='editar_perfil'),
]
