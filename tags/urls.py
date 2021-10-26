from django.contrib import admin
from django.urls import path

from .views import URLViewSet

url_create = URLViewSet.as_view({
    'post': 'create'
})
url_detail = URLViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', url_create, name='url_create'),
    path('<pk>/', url_detail, name='url_detail'),
]