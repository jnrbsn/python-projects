"""A web app for fetching the current weather for a given location."""

import flask

from .exceptions import WeatherError
from .utils import geocode, get_current_weather


app = flask.Flask(__name__)


@app.route('/')
def index():
    """The main index for the app."""
    query = flask.request.args.get('q') or ''
    error = None
    geo_data = {}
    weather_data = {}

    try:
        if query:
            geo_data = geocode(query)
            if geo_data:
                weather_data = get_current_weather(geo_data['lat'], geo_data['lon'])
            else:
                raise WeatherError('No location found that matches the search query.')
    except WeatherError as ex:
        error = str(ex)

    return flask.render_template(
        'index.html',
        query=query,
        error=error,
        geo_data=geo_data,
        weather_data=weather_data,
    )


def run():
    """Run the flask app."""
    app.debug = True
    app.run()
