from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('astro_project.api.urls')),
    path('api/horoscope', views.get_horoscope, name='get_horoscope'),
] 