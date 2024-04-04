import random

import requests
from requests.exceptions import RequestException
from retry import retry


@retry(RequestException, tries=2, delay=2, backoff=2, max_delay=10)
def get_weather_from_open_meteo(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=precipitation"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()["hourly"]


def random_rain_decision():
    return random.choice([True, False])


def is_raining(hourly_data, check_time):
    time_data = hourly_data.get("time", [])
    precipitation_data = hourly_data.get("precipitation", [])
    if check_time in time_data:
        index = time_data.index(check_time)
        return (
            precipitation_data[index] > 0
        )  # It's raining if precipitation is greater than 0
    else:
        return False


def get_weather_with_fallback(latitude, longitude, check_time):
    try:
        hourly_weather = get_weather_from_open_meteo(latitude, longitude)
        return is_raining(hourly_weather, check_time)
    except RequestException:
        return random_rain_decision()
