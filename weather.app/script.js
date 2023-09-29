
const apiKey = 'YOUR_API_KEY'; // Replace with your API key

const submitButton = document.getElementById('submit-btn');
const locationInput = document.getElementById('location-input');
const currentWeatherDiv = document.getElementById('current-weather');
const forecastWeatherDiv = document.getElementById('forecast-weather');

submitButton.addEventListener('click', () => {
  const location = locationInput.value;
  if (location.trim() === '') {
    alert('Please enter a location');
    return;
  }

  fetchWeather(location);
});

async function fetchWeather(location) {
  try {
    // Fetch current weather data
    const currentWeatherURL = `https://api.weatherapi.com/v1/current.json?key=${apiKey}&q=${location}&aqi=no`;
    const currentWeatherResponse = await fetch(currentWeatherURL);
    const currentWeatherData = await currentWeatherResponse.json();

    // Fetch forecast weather data
    const forecastWeatherURL = `https://api.weatherapi.com/v1/forecast.json?key=${apiKey}&q=${location}&days=3`;
    const forecastWeatherResponse = await fetch(forecastWeatherURL);
    const forecastWeatherData = await forecastWeatherResponse.json();

    // Display current weather
    displayCurrentWeather(currentWeatherData);

    // Display forecast weather
    displayForecastWeather(forecastWeatherData);
  } catch (error) {
    console.log('Error:', error);
    alert('An error occurred while fetching weather data');
  }
}

function displayCurrentWeather(data) {
  const location = data.location.name;
  const tempC = data.current.temp_c;
  const condition = data.current.condition.text;

  currentWeatherDiv.innerHTML = `
    <h3>Current Weather</h3>
    <p>Location: ${location}</p>
    <p>Temperature: ${tempC}°C</p>
    <p>Condition: ${condition}</p>
  `;
}

function displayForecastWeather(data) {
  const forecast = data.forecast.forecastday;
  let forecastHTML = '<h3>Forecast Weather</h3>';

  forecast.forEach(day => {
    const date = day.date;
    const maxTempC = day.day.maxtemp_c;
    const minTempC = day