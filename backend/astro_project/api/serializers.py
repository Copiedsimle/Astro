from rest_framework import serializers
from .models import Horoscope

class HoroscopeSerializer(serializers.ModelSerializer):
    sign_display = serializers.CharField(source='get_sign_display', read_only=True)
    
    class Meta:
        model = Horoscope
        fields = ['id', 'sign', 'sign_display', 'date', 'prediction', 'created_at']
        read_only_fields = ['id', 'created_at'] 