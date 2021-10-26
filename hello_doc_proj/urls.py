from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import settings


urlpatterns = [
    path('tags/', include('tags.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)