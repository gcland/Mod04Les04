class WeatherDataFetcher:
    def __init__(self, city):
        self.city = city
        self.weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
    }
    def get_weather_data(self, city):
        return(self.weather_data[city])
        

