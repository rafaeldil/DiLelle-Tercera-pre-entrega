from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from inicio import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('usuarios/', include('usuarios.urls')),
    # path('productos/', include('productos.urls')),
    # path('mensajeria/', include('mensajeria.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
