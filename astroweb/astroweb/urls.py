from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import BirthDetailsViewSet, get_zodiac_details

router = DefaultRouter()
router.register(r'birth-details', BirthDetailsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('zodiac-details/<str:sign>/', get_zodiac_details, name='zodiac-details'),
]