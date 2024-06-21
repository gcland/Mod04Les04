from WeatherDataFetcher import WeatherDataFetcher
from DataParser import DataParser

class UserInterface:
    def __init__(self):
        self

    def ask_city(self):
        while True:
            try:
                choice = input("Choose city from New York, London, or Tokyo, or 'quit' to quit: ")
                if choice.lower() == 'quit':
                    break
                elif choice not in ['New York', 'London', 'Tokyo']:
                    raise ValueError('Invalid choice.')
                else:
                    city = WeatherDataFetcher(choice)
                    city.get_weather_data(choice)
                    data = DataParser(city)
                    data.get_detailed_forecast(city, choice)
            except Exception as e:
                print(e)

city = UserInterface()
city.ask_city()

