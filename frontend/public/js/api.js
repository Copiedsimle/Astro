// API connections to the Django backend

const API_BASE_URL = 'http://localhost:8000/api';

// Function to fetch daily horoscope for a sign
async function getDailyHoroscope(sign) {
  try {
    const response = await fetch(`${API_BASE_URL}/horoscopes/${sign}/`);
    
    if (!response.ok) {
      throw new Error(`Error: ${response.status}`);
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching horoscope:', error);
    return null;
  }
}

// Function to fetch all horoscopes
async function getAllHoroscopes() {
  try {
    const response = await fetch(`${API_BASE_URL}/horoscopes/`);
    
    if (!response.ok) {
      throw new Error(`Error: ${response.status}`);
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching all horoscopes:', error);
    return [];
  }
} 