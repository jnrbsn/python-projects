"""Custom exception classes."""


class WeatherError(Exception):
    """Generic exception for this app."""
    pass


class OpenStreetMapError(WeatherError):
    """Raised because of an error getting data from OpenStreetMap."""
    pass


class OpenWeatherMapError(WeatherError):
    """Raised because of an error getting data from OpenWeatherMap."""
    pass
