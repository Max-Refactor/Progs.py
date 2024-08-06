from CodeFeatures import *
from prettytable import PrettyTable
import requests

def get_weather(lang: str = 'en') -> None:
    print('lang: ', lang)

    if lang == 'ru': city = input('Введите город, в котором хотите узнать погоду: ')
    elif lang == 'ua': city = input('Введіть місто, де хочете дізнатися погоду: ')
    else: city = input('Enter the city where you want to check the weather: ')

    clearConsole()
    tprint('Progs.py')

    api_key = '79d1ca96933b0328e1c7e3e7a26cb347'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,  # Название города
        'units': 'metric',  # Единицы измерения - метрические
        'lang': lang,  # Язык ответа
        'appid': api_key  # Ключ API
    }

    try:
        # Выполняем GET-запрос с параметрами
        response = requests.get(base_url, params=params)
        # Проверяем успешность выполнения запроса
        response.raise_for_status()
        # Преобразуем ответ в формат JSON
        weather_data = response.json()

        # Получаем текущую температуру
        temperature = weather_data['main']['temp']
        # Получаем ощущаемую температуру
        temperature_feels = weather_data['main']['feels_like']
        # Получаем скорость ветра
        wind_speed = weather_data['wind']['speed']
        # Получаем описание облачности
        cloud_cover = weather_data['weather'][0]['description']
        # Получаем влажность
        humidity = weather_data['main']['humidity']

        if lang == 'ru':
            weather_table = PrettyTable()
            weather_table.field_names = ['Город:', 'Температура воздуха:', 'Ощущается как:', 'Скорость ветра:', 'Погода:', 'Влажность:']
            weather_table.add_row([city, f'{temperature}C°', f'{temperature_feels}C°', f'{wind_speed} м/с', cloud_cover, f'{humidity}%'])

        elif lang == 'ua':
            weather_table = PrettyTable()
            weather_table.field_names = ['Місто:', 'Температура повітря:', 'Відчувається як:', 'Швидкість вітру:', 'Погода:', 'Вологість:']
            weather_table.add_row([city, f'{temperature}C°', f'{temperature_feels}C°', f'{wind_speed} м/с', cloud_cover, f'{humidity}%'])

        else:
            weather_table = PrettyTable()
            weather_table.field_names = ['City:', 'Air temperature:', 'Feels like:', 'Wind speed:', 'Weather:', 'Humidity:']
            weather_table.add_row([city, f'{temperature}C°', f'{temperature_feels}C°', f'{wind_speed} m/s', cloud_cover, f'{humidity}%'])

        print(weather_table)

    # Обрабатываем исключения, связанные с запросом
    except requests.RequestException as e:
        print(f'Error when requesting weather: {e}')
    # Обрабатываем случаи отсутствия данных в ответе
    except KeyError:
        print(f'Could not determine the city: {city}')


if __name__ == "__main__":
    get_weather()
