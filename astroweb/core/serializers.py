from rest_framework import serializers
from .models import BirthDetails

class BirthDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirthDetails
        fields = ['id', 'user_id', 'birth_date', 'birth_time', 'birth_place', 'created_at', 'zodiac_sign', 'life_path_number']