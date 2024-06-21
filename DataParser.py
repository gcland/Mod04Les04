from WeatherDataFetcher import WeatherDataFetcher

class DataParser:
    def __init__(self, city):
        self.city = city
    
    def parse_weather_data(self, city, data):
        if not data:
            return "Weather data not available"
        else:
            print(f"Fetching weather data for {city}...")
            temperature = data["temperature"]
            condition = data["condition"]
            humidity = data["humidity"]
            print(f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%")

    def get_detailed_forecast(self, city, choice):
        return self.parse_weather_data(city.city, city.weather_data[choice])
        