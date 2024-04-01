import requests

API_KEY = 'f7eebb92f92d09e4ca7908df1c72aa0e'
user_input = input('Enter a city name:')
weather_inf = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={API_KEY}"
)

if weather_inf.status_code == 404:
  print('City not found')
else:
  weather = (weather_inf.json()['weather'][0]['main'])
  temp = round(weather_inf.json()['main']['temp'])
  print(
      f'The weather in {user_input} is {weather} and the temperature is {temp} degrees farenheit,Have a good day!')
  
