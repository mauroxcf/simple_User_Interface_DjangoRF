from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('api/v1/', include('app.urls', namespace='app'),),
]
