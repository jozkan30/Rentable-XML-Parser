require 'open-uri'
require 'json'
require 'pry'

def get_weather(lat, long)
  url = "https://api.weather.gov/points/#{lat},#{long}"
  puts "Fetching Weather for location #{lat}, #{long}"
  uri = URI.open(url).read
  data = JSON.parse(uri)
  forecast = data['properties']['forecast']
  forecast_uri = URI.open(forecast).read
  forecast_data = JSON.parse(forecast_uri)
  today = forecast_data['properties']['periods'][0]
  weather = today['detailedForecast']
  weather
end