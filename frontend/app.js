const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

// View engine setup
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Middleware
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));
app.use('/css', express.static(path.join(__dirname, 'css')));
app.use('/js', express.static(path.join(__dirname, 'js')));

// Routes
app.get('/', (req, res) => {
  res.render('home', { 
    title: 'Astrology & Horoscope'
  });
});

app.get('/daily-horoscope', (req, res) => {
  res.render('daily_horoscope', { 
    title: 'Daily Horoscope'
  });
});

// Start server
app.listen(port, () => {
  console.log(`Frontend server running at http://localhost:${port}`);
});