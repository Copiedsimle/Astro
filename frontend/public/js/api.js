// API connections to the Django backend

const API_BASE_URL = 'http://localhost:8000/api';

// Function to fetch daily horoscope for a sign
async function getDailyHoroscope(sign) {
    try {
        const response = await fetch(`${API_BASE_URL}/horoscope/${sign}/`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        // If no horoscope data, provide a default message
        if (!data.horoscope) {
            data.horoscope = "The stars are aligned for you today. Trust your instincts and embrace new opportunities.";
        }
        return data;
    } catch (error) {
        console.error('Error fetching horoscope:', error);
        throw error;
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

// Function to fetch horoscope for a sign
async function fetchHoroscope(sign) {
    try {
        const response = await fetch(`http://localhost:8000/api/horoscope/${sign}`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return await response.json();
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}