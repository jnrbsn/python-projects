from setuptools import setup

from weather import __version__

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='weather',
    version=__version__,
    description='A web app for fetching the current weather for a given location.',
    long_description=long_description,
    url='https://github.com/jnrbsn/python-projects/tree/master/web/weather',
    author='Jonathan Robson',
    author_email='jnrbsn@gmail.com',
    packages=['weather'],
    install_requires=[
        'Flask==0.10.1',
        'requests==2.3.0',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'weather-server=weather.app:run'
        ],
    },
)
