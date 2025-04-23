from django.urls import path
from . import views

urlpatterns = [
    path('horoscopes/', views.horoscope_list),
    path('horoscopes/<str:sign>/', views.horoscope_detail),
] 