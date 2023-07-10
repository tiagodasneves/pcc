from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doacao/', include('doacao.urls')),
    path('auth/', include('usuarios.urls')),
]