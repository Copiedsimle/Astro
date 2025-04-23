from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Horoscope
from .serializers import HoroscopeSerializer
from datetime import date

@api_view(['GET', 'POST'])
def horoscope_list(request):
    if request.method == 'GET':
        horoscopes = Horoscope.objects.all()
        serializer = HoroscopeSerializer(horoscopes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = HoroscopeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def horoscope_detail(request, sign):
    try:
        # Get today's horoscope for the specified sign
        today = date.today()
        horoscope = Horoscope.objects.filter(sign=sign, date=today).first()
        
        if horoscope is None:
            # If no horoscope for today, return the most recent one
            horoscope = Horoscope.objects.filter(sign=sign).order_by('-date').first()
        
        if horoscope is None:
            return Response({"error": "No horoscope found for this sign"}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = HoroscopeSerializer(horoscope)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 