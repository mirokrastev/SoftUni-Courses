const forecastDiv = document.getElementById('forecast');
const mapper = {
    'Sunny': '&#x2600',
    'Partly sunny': ' &#x26C5',
    'Overcast': '&#x2601',
    'Rain': '&#x2614',
    'Degrees': '&#176'
}

function attachEvents() {
    let submitButton = document.getElementById('submit');
    submitButton.addEventListener('click', main);
}

async function main() {
    let cityName = document.querySelector('#location').value;
    const url = `http://localhost:3030/jsonstore/forecaster/locations`;

    let response = await fetch(url);
    let json = await response.json();

    forecastDiv.style.display = 'block';

    let city = json.find(e => e.name === cityName);

    if (!city) {
        return;
    }

    let [today, upcoming] = await Promise.all([
        fetch(`http://localhost:3030/jsonstore/forecaster/today/${city.code}`)
            .then(response => response.json()),
        fetch(`http://localhost:3030/jsonstore/forecaster/upcoming/${city.code}`)
            .then(response => response.json())
    ]);

    produceForecast(today, upcoming);
}

function produceForecast(todayForecast, upcomingForecast) {
    console.log(upcomingForecast);
    forecastDiv.querySelector('#current').innerHTML += `
    <div class="forecasts">
        <span class="condition symbol">${mapper[todayForecast.forecast.condition]}</span>      
        <span class="condition">
            <span class="forecast-data">${todayForecast.name}</span>
            <span class="forecast-data">${todayForecast.forecast.low}°/${todayForecast.forecast.high}°</span>
            <span class="forecast-data">${todayForecast.forecast.condition}</span>
        </span>  
    </div>`;
    let upcomingForecastsDiv = document.createElement('div');
    upcomingForecastsDiv.className = 'forecast-info';

    upcomingForecast.forecast.forEach(obj => {
        upcomingForecastsDiv.innerHTML += `
        <span class="upcoming">
            <span class="condition">
                <span class="symbol">${mapper[obj.condition]}</span>
                <span class="forecast-data">${todayForecast.forecast.low}°/${todayForecast.forecast.high}°</span>
                <span class="forecast-data">${todayForecast.forecast.condition}</span>
            </span>
        </span>`
    })

    forecastDiv.querySelector('#upcoming').appendChild(upcomingForecastsDiv);
}

attachEvents();