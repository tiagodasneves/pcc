from django.urls import path
from . import views

urlpatterns = [
    path('questionario', views.quest, name='quest'),
    path('resultado', views.result, name='result'),
    path('resultados', views.resultados, name='resultados'),
    path('', views.home, name='home'),
]
