import requests


WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'
API = '67a58c8f10d5e85b516cc7cfee622679'
CITY_NAME = 'Khabarovsk'


def weather():
    params = {
        'q': CITY_NAME,
        'appid': API,
        'units': 'metric',
        'lang': 'ru'
    }

    response = requests.get(WEATHER_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        print(f'Город: {city}')
        print(f'Погода: {description}')
        print(f'Температура: {round(temperature)} °C')
        print(f'Влажность: {humidity}%')
        print(f'Давление: {pressure} мбар')
        print(f'Скорость ветра: {wind_speed} м/с')
    else:
        print('Ошибка:', response.status_code)


if __name__ == '__main__':
    weather()