import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [formData, setFormData] = useState({
    user_id: '',
    birth_date: '',
    birth_time: '',
    birth_place: '',
    latitude: '',
    longitude: '',
  });
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const [selectedSign, setSelectedSign] = useState('');
  const [zodiacDetails, setZodiacDetails] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setResult(null);
    setLoading(true);

    try {
      const response = await axios.post('http://localhost:8000/birth-details/', formData, {
        headers: { 'Content-Type': 'application/json' },
      });
      console.log('Response:', response.data);
      if (response.status === 201) {
        setResult(response.data);
      }
    } catch (err) {
      console.error('Error:', err.response ? err.response.data : err.message);
      setError(err.response?.data?.error || 'Error submitting data. Please check your input or server status.');
    } finally {
      setLoading(false);
    }
  };

  const handleSignChange = async (e) => {
    const sign = e.target.value;
    setSelectedSign(sign);
    if (sign) {
      try {
        const response = await axios.get(`http://localhost:8000/zodiac-details/${sign}/`);
        setZodiacDetails(response.data);
      } catch (err) {
        console.error('Error fetching zodiac details:', err);
        setZodiacDetails({ error: 'Failed to load details.' });
      }
    } else {
      setZodiacDetails(null);
    }
  };

  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4">Find Your Astro Sign and Number</h1>
      <form onSubmit={handleSubmit} className="p-4 border rounded">
        <div className="mb-3">
          <input
            type="number"
            name="user_id"
            value={formData.user_id}
            onChange={handleChange}
            className="form-control"
            placeholder="User ID"
            required
          />
        </div>
        <div className="mb-3">
          <input
            type="date"
            name="birth_date"
            value={formData.birth_date}
            onChange={handleChange}
            className="form-control"
            required
          />
        </div>
        <div className="mb-3">
          <input
            type="time"
            name="birth_time"
            value={formData.birth_time}
            onChange={handleChange}
            className="form-control"
            required
          />
        </div>
        <div className="mb-3">
          <input
            type="text"
            name="birth_place"
            value={formData.birth_place}
            onChange={handleChange}
            className="form-control"
            placeholder="Birth Place"
            required
          />
        </div>
        <div className="mb-3">
          <input
            type="number"
            name="latitude"
            value={formData.latitude}
            onChange={handleChange}
            className="form-control"
            placeholder="Latitude (e.g., 40.7128)"
            step="0.0001"
            required
          />
        </div>
        <div className="mb-3">
          <input
            type="number"
            name="longitude"
            value={formData.longitude}
            onChange={handleChange}
            className="form-control"
            placeholder="Longitude (e.g., -74.0060)"
            step="0.0001"
            required
          />
        </div>
        <button type="submit" className="btn btn-primary" disabled={loading}>
          {loading ? 'Submitting...' : 'Submit'}
        </button>
      </form>

      {error && <p className="text-danger mt-3">{error}</p>}
      {result && (
        <div className="mt-4 p-3 border results">
          <h2>Results</h2>
          <p><strong>Zodiac Sign:</strong> {result.zodiac_sign}</p>
          <p><strong>Life Path Number:</strong> {result.life_path_number}</p>
          <p><strong>Astrology Prediction:</strong> {result.astrology_prediction}</p>
        </div>
      )}

      <div className="mt-4 p-3 border">
        <h2>Select Zodiac Sign for Details</h2>
        <select
          value={selectedSign}
          onChange={handleSignChange}
          className="form-control mb-3"
          style={{ maxWidth: '300px' }}
        >
          <option value="">Select a Zodiac Sign</option>
          <option value="Aries">Aries</option>
          <option value="Taurus">Taurus</option>
          <option value="Gemini">Gemini</option>
          <option value="Cancer">Cancer</option>
          <option value="Leo">Leo</option>
          <option value="Virgo">Virgo</option>
          <option value="Libra">Libra</option>
          <option value="Scorpio">Scorpio</option>
          <option value="Sagittarius">Sagittarius</option>
          <option value="Capricorn">Capricorn</option>
          <option value="Aquarius">Aquarius</option>
          <option value="Pisces">Pisces</option>
        </select>

        {zodiacDetails && (
          <div className="mt-3">
            <h3>Details for {selectedSign}</h3>
            <div className="card">
              <div className="card-body">
                <div className="mb-3">
                  <h4>Traits</h4>
                  <p>{zodiacDetails.traits}</p>
                </div>
                
                <div className="mb-3">
                  <h4>Monthly Horoscope - {zodiacDetails.monthly_horoscope?.month}</h4>
                  <p>{zodiacDetails.monthly_horoscope?.description}</p>
                </div>

                <div className="mb-3">
                  <h4>Basic Information</h4>
                  <p><strong>Element:</strong> {zodiacDetails.element}</p>
                  <p><strong>Lucky Number:</strong> {zodiacDetails.lucky_number}</p>
                  <p><strong>Compatible Signs:</strong> {zodiacDetails.compatible_signs?.join(', ')}</p>
                </div>

                <div className="mb-3">
                  <h4>Remedies</h4>
                  <div className="remedies-grid">
                    <div className="remedy-item">
                      <h5>Gemstones</h5>
                      <p>{zodiacDetails.remedies?.gemstones}</p>
                    </div>
                    <div className="remedy-item">
                      <h5>Rudraksha</h5>
                      <p>{zodiacDetails.remedies?.rudraksha}</p>
                    </div>
                    <div className="remedy-item">
                      <h5>Yantra</h5>
                      <p>{zodiacDetails.remedies?.yantra}</p>
                    </div>
                    <div className="remedy-item">
                      <h5>Mantra</h5>
                      <p>{zodiacDetails.remedies?.mantra}</p>
                    </div>
                    <div className="remedy-item">
                      <h5>Puja</h5>
                      <p>{zodiacDetails.remedies?.puja}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      <style>
        {`
          .remedies-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
          }
          
          .remedy-item {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 8px;
          }
          
          .remedy-item h5 {
            color: #2c3e50;
            margin-bottom: 0.5rem;
          }
          
          .card {
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border: none;
            border-radius: 10px;
          }
          
          .card-body {
            padding: 2rem;
          }
          
          h4 {
            color: #2c3e50;
            margin-bottom: 1rem;
            border-bottom: 2px solid #e9ecef;
            padding-bottom: 0.5rem;
          }
        `}
      </style>
    </div>
  );
}

export default App;