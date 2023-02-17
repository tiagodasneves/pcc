from django.urls import path
from . import views
from .views import home_view

urlpatterns = (
    path('', views.home_view, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login')
)