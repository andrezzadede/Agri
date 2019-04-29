from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from eventos import urls as eventos_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventos/', include(eventos_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
