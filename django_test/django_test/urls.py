from django.contrib import admin
from django.urls import path, include
from api import views


urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]

