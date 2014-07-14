"""Utility functions for weather app."""

import requests

from .exceptions import OpenStreetMapError, OpenWeatherMapError


def geocode(query):
    """Get the geographic coordinates of a location."""
    response = requests.get(
        'http://nominatim.openstreetmap.org/search',
        params={'q': query, 'format': 'json'}
    )

    if response.status_code != 200:
        raise OpenStreetMapError(
            'Got non-OK status code {0} from OpenStreetMap.'.format(response.status_code))

    data = response.json()

    if not data:
        return None

    return data[0]


def get_current_weather(lat, lon):
    """Get the current weather for a set of geographic coordinates."""
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather',
        params={'lat': lat, 'lon': lon, 'units': 'metric'}
    )

    if response.status_code != 200:
        raise OpenWeatherMapError(
            'Got non-OK status code {0} from OpenWeatherMap.'.format(response.status_code))

    data = response.json()

    if not data:
        return None

    data['wind']['direction'] = degrees_to_direction(data['wind']['deg'])

    return data


def degrees_to_direction(degrees):
    """Convert degrees to a compass direction."""
    directions = [
        'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
        'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW',
    ]
    return directions[int(round(float(degrees) / 22.5)) % 16]
