import requests
# Pull weather data based on Longitude and Latitude from XML. From response pull endpoint for 12 hour forecasts for the next 7 days. From this response pull today's weather as string value

def get_weather(lat, long):
    url =  f'https://api.weather.gov/points/{lat},{long}'
    print(f'Fetching Weather for location {lat}, {long}')
    req = requests.get(url)
    assert req.status_code == 200,f"Unable to get weather data: {req.status_code}"
    resp = req.json()
    forecast = resp['properties']['forecast']
    fetch_forecast = requests.get(forecast).json()
    today = fetch_forecast['properties'].get('periods')[0]
    weather = today.get('detailedForecast')
    return weather