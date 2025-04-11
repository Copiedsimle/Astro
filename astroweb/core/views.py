import swisseph as swe
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BirthDetails
from .serializers import BirthDetailsSerializer
from datetime import datetime, date
import os
from gpt4all import GPT4All
from django.conf import settings

# Set ephemeris path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SWE_EPHE_PATH = os.path.join(BASE_DIR, 'ephem_data', 'ephe')
swe.set_ephe_path(SWE_EPHE_PATH)

# Initialize GPT4All model
try:
    model = GPT4All("ggml-gpt4all-j-v1.3-groovy")
except Exception as e:
    print(f"Warning: GPT4All model initialization failed: {e}")
    model = None

# Zodiac sign default information
ZODIAC_INFO = {
    "Aries": {
        "traits": "Bold, ambitious, and energetic. Natural leaders with a dynamic personality.",
        "element": "Fire",
        "lucky_number": 9,
        "compatible_signs": ["Leo", "Sagittarius"],
        "remedies": {
            "gemstones": "Red Coral, Ruby",
            "rudraksha": "3 Mukhi",
            "yantra": "Mars Yantra",
            "mantra": "Om Hreem Hum Namah",
            "puja": "Hanuman Puja"
        }
    },
    "Taurus": {
        "traits": "Patient, reliable, and determined. Known for practicality and love of comfort.",
        "element": "Earth",
        "lucky_number": 6,
        "compatible_signs": ["Virgo", "Capricorn"],
        "remedies": {
            "gemstones": "Diamond, White Sapphire",
            "rudraksha": "5 Mukhi",
            "yantra": "Venus Yantra",
            "mantra": "Om Shum Shukraya Namah",
            "puja": "Lakshmi Puja"
        }
    },
    "Gemini": {
        "traits": "Versatile, expressive, and curious. Quick learners with excellent communication skills.",
        "element": "Air",
        "lucky_number": 5,
        "compatible_signs": ["Libra", "Aquarius"],
        "remedies": {
            "gemstones": "Emerald, Jade",
            "rudraksha": "6 Mukhi",
            "yantra": "Mercury Yantra",
            "mantra": "Om Bum Budhaya Namah",
            "puja": "Vishnu Puja"
        }
    },
    "Cancer": {
        "traits": "Nurturing, intuitive, and emotional. Deep connection to home and family.",
        "element": "Water",
        "lucky_number": 2,
        "compatible_signs": ["Scorpio", "Pisces"],
        "remedies": {
            "gemstones": "Pearl, Moonstone",
            "rudraksha": "2 Mukhi",
            "yantra": "Moon Yantra",
            "mantra": "Om Shraam Shreem Shroum Sah Chandraya Namah",
            "puja": "Shiva Puja"
        }
    },
    "Leo": {
        "traits": "Confident, generous, and charismatic. Natural performers with strong leadership qualities.",
        "element": "Fire",
        "lucky_number": 1,
        "compatible_signs": ["Aries", "Sagittarius"],
        "remedies": {
            "gemstones": "Ruby, Garnet",
            "rudraksha": "5 Mukhi",
            "yantra": "Sun Yantra",
            "mantra": "Om Hrim Hum Suryaya Namah",
            "puja": "Surya Puja"
        }
    },
    "Virgo": {
        "traits": "Analytical, practical, and meticulous. Perfectionists with a strong sense of duty.",
        "element": "Earth",
        "lucky_number": 5,
        "compatible_signs": ["Taurus", "Capricorn"],
        "remedies": {
            "gemstones": "Emerald, Green Tourmaline",
            "rudraksha": "5 Mukhi",
            "yantra": "Mercury Yantra",
            "mantra": "Om Bum Budhaya Namah",
            "puja": "Vishnu Puja"
        }
    },
    "Libra": {
        "traits": "Diplomatic, harmonious, and fair-minded. Natural mediators with a love for beauty.",
        "element": "Air",
        "lucky_number": 6,
        "compatible_signs": ["Gemini", "Aquarius"],
        "remedies": {
            "gemstones": "Diamond, White Sapphire",
            "rudraksha": "6 Mukhi",
            "yantra": "Venus Yantra",
            "mantra": "Om Shum Shukraya Namah",
            "puja": "Lakshmi Puja"
        }
    },
    "Scorpio": {
        "traits": "Passionate, resourceful, and mysterious. Deep thinkers with powerful intuition.",
        "element": "Water",
        "lucky_number": 8,
        "compatible_signs": ["Cancer", "Pisces"],
        "remedies": {
            "gemstones": "Red Coral, Garnet",
            "rudraksha": "8 Mukhi",
            "yantra": "Mars Yantra",
            "mantra": "Om Jum Sah Ketave Namah",
            "puja": "Hanuman Puja"
        }
    },
    "Sagittarius": {
        "traits": "Optimistic, adventurous, and philosophical. Freedom-loving with a thirst for knowledge.",
        "element": "Fire",
        "lucky_number": 3,
        "compatible_signs": ["Aries", "Leo"],
        "remedies": {
            "gemstones": "Yellow Sapphire, Topaz",
            "rudraksha": "5 Mukhi",
            "yantra": "Jupiter Yantra",
            "mantra": "Om Gum Gurave Namah",
            "puja": "Vishnu Puja"
        }
    },
    "Capricorn": {
        "traits": "Ambitious, disciplined, and patient. Natural managers with strong determination.",
        "element": "Earth",
        "lucky_number": 8,
        "compatible_signs": ["Taurus", "Virgo"],
        "remedies": {
            "gemstones": "Blue Sapphire, Amethyst",
            "rudraksha": "7 Mukhi",
            "yantra": "Saturn Yantra",
            "mantra": "Om Pram Preem Praum Sah Shanaye Namah",
            "puja": "Hanuman Puja"
        }
    },
    "Aquarius": {
        "traits": "Progressive, original, and humanitarian. Independent thinkers with innovative ideas.",
        "element": "Air",
        "lucky_number": 4,
        "compatible_signs": ["Gemini", "Libra"],
        "remedies": {
            "gemstones": "Blue Sapphire, Lapis Lazuli",
            "rudraksha": "7 Mukhi",
            "yantra": "Saturn Yantra",
            "mantra": "Om Sham Shanaishcharaya Namah",
            "puja": "Shiva Puja"
        }
    },
    "Pisces": {
        "traits": "Intuitive, artistic, and compassionate. Dreamers with deep emotional understanding.",
        "element": "Water",
        "lucky_number": 7,
        "compatible_signs": ["Cancer", "Scorpio"],
        "remedies": {
            "gemstones": "Yellow Sapphire, Amethyst",
            "rudraksha": "4 Mukhi",
            "yantra": "Jupiter Yantra",
            "mantra": "Om Gum Gurave Namah",
            "puja": "Vishnu Puja"
        }
    }
}

@api_view(['GET'])
def get_zodiac_details(request, sign):
    if sign not in ZODIAC_INFO:
        return Response({"error": "Invalid zodiac sign."}, status=status.HTTP_400_BAD_REQUEST)

    # Get base information from our default data
    details = ZODIAC_INFO[sign].copy()
    
    # Add monthly horoscope
    try:
        if model:
            # Generate monthly horoscope using GPT4All
            prompt = f"Write a positive and uplifting monthly horoscope for {sign} for April 2025. Focus on career, relationships, and personal growth. Keep it around 100 words."
            try:
                response = model.generate(prompt, max_tokens=200)
                horoscope = response.strip()
            except Exception as e:
                print(f"Error generating horoscope with GPT4All: {e}")
                horoscope = f"April 2025 brings exciting opportunities for {sign}. Focus on your personal growth and maintain balance in all aspects of life. Your natural {details['traits'].lower()} will help you overcome challenges and achieve success."
        else:
            # Fallback horoscope if model is not available
            horoscope = f"April 2025 brings positive energy and opportunities for growth. Your {details['element']} element will guide you towards success."
    except Exception as e:
        print(f"Error generating horoscope: {e}")
        horoscope = f"April 2025 brings positive energy and opportunities for growth. Your {details['element']} element will guide you towards success."

    details["monthly_horoscope"] = {
        "month": "April 2025",
        "description": horoscope
    }
    
    return Response(details, status=status.HTTP_200_OK)

class BirthDetailsViewSet(viewsets.ModelViewSet):
    queryset = BirthDetails.objects.all()
    serializer_class = BirthDetailsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data['birth_date'] > date.today():
                return Response({"error": "Birth date cannot be in the future."}, status=status.HTTP_400_BAD_REQUEST)
            try:
                self.perform_create(serializer)
                instance = serializer.instance

                lat = float(instance.latitude)
                lon = float(instance.longitude)

                birth_date = datetime.combine(instance.birth_date, instance.birth_time if instance.birth_time else datetime.min.time())
                jd = swe.julday(birth_date.year, birth_date.month, birth_date.day, birth_date.hour + birth_date.minute / 60.0)

                sun_pos = swe.calc_ut(jd, swe.SUN)[0][0]
                moon_pos = swe.calc_ut(jd, swe.MOON)[0][0]
                houses = swe.houses_ex(jd, lat, lon, b'+')[0]
                ascendant = houses[0]

                zodiac_sign = self._get_zodiac_sign(sun_pos)
                moon_sign = self._get_zodiac_sign(moon_pos)
                asc_sign = self._get_zodiac_sign(ascendant)

                prediction = self._generate_prediction(zodiac_sign, moon_sign, asc_sign)

                instance.zodiac_sign = zodiac_sign
                instance.life_path_number = self._calculate_life_path_number(instance.birth_date)
                instance.astrology_prediction = prediction
                instance.save()

                serialized_data = self.get_serializer(instance).data
                return Response(serialized_data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": f"Calculation failed: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _get_zodiac_sign(self, longitude):
        degrees = longitude % 360
        zodiac_ranges = [
            ("Aries", 0, 30), ("Taurus", 30, 60), ("Gemini", 60, 90),
            ("Cancer", 90, 120), ("Leo", 120, 150), ("Virgo", 150, 180),
            ("Libra", 180, 210), ("Scorpio", 210, 240), ("Sagittarius", 240, 270),
            ("Capricorn", 270, 300), ("Aquarius", 300, 330), ("Pisces", 330, 360)
        ]
        for sign, start, end in zodiac_ranges:
            if start <= degrees < end:
                return sign
        return "Unknown"

    def _calculate_life_path_number(self, birth_date):
        date_str = birth_date.strftime("%d%m%Y")
        total = sum(int(digit) for digit in date_str)
        while total > 9 and total not in [11, 22]:
            total = sum(int(digit) for digit in str(total))
        return total

    def _generate_prediction(self, sun_sign, moon_sign, asc_sign):
        base = f"As a {sun_sign}, you are driven by traits of ambition and creativity."
        moon_influence = f"The Moon in {moon_sign} enhances your emotional intuition this month."
        asc_influence = f"Your {asc_sign} rising sign suggests a charismatic public presence."
        trend = "The Swiss Ephemeris data indicates a favorable alignment, suggesting growth ahead."
        return f"{base} {moon_influence} {asc_influence} {trend}"