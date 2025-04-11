# Astro Web Application

A Django-based web application for generating personalized horoscopes and astrological predictions using GPT4All for local AI-powered content generation.

## Features

- Zodiac sign details and characteristics
- Monthly horoscope generation using local AI (GPT4All)
- Birth chart calculations using Swiss Ephemeris
- Life path number calculations
- Astrological predictions and compatibility checks

## Technical Stack

- Backend: Django with Django REST Framework
- Frontend: React.js
- AI: GPT4All (local language model)
- Astrological Calculations: Swiss Ephemeris
- Database: SQLite (default)

## Setup

1. Clone the repository:
```bash
git clone [your-repository-url]
cd astro
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
cd astro-frontend
npm install
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. In a separate terminal, start the frontend:
```bash
cd astro-frontend
npm start
```

## Note

This application uses GPT4All for local AI-powered horoscope generation, eliminating the need for external API keys or cloud services. The model will be downloaded automatically on first use.