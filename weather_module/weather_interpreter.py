# fetching weather data from the openweathermap API
import os, requests, json

# setting openweathermap API key and URL for Indiana
# plus imperial units bc america i guess
weather_key = os.environ.get('weather_api_key')
weather_url = f'http://api.openweathermap.org/data/2.5/weather?id=5194868&appid={weather_key}&units=imperial'

# fetches the weather from openweathermap API
# returns measured temperature and "real-feel" temperature
def weather_collector():
    print('IT\'S WEATHER TIME')
    
    response = requests.get(weather_url)
    weather_data = response.json()

    # error codes go brrrr
    if weather_data['cod'] not in ['401', '404', '429', '500', '502', '503', '504',]:
        main = weather_data['main']
        current_temp = main['temp']

        condition_main = weather_data['weather']
        condition_json = condition_main[0]

        condition = condition_json['icon']

        return current_temp, condition

    elif weather_data['cod'] == '401':
        print('401 error, api key invalid')
    elif weather_data['cod'] == '404':
        print('404 error, collecting data with invalide city code')
    elif weather_data['cod'] == '429':
        print('429 error, too many requests submitted')
    else:
        print('probably a 50X code or something good luck m8 send some emails')