import requests
from django.http import JsonResponse

def get_horoscope(request):
    sign = request.GET.get('sign', '').capitalize()
    if not sign:
        return JsonResponse({'error': 'Please provide a zodiac sign'}, status=400)

    # Replace with your API key and endpoint
    api_url = f"9K7oBnvsVf1lDYOOm1Xtl4KkVqrb7tR28OwTNCU3"
    headers = {
        'Authorization': 'Bearer YOUR_API_KEY'
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        horoscope = data.get('horoscope', 'No horoscope data available.')
        return JsonResponse({'sign': sign, 'horoscope': horoscope})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': 'Failed to fetch horoscope data'}, status=500)