from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOMORROWIO_TOKEN')

DEFAULT_CORDS = '55.7522,37.6156'

URL = 'https://api.tomorrow.io/v4/weather/forecast?location={coord}&timesteps=1m&apikey={TOKEN}'

EXAMPLE_DICT = {
  'Moscow': '55.7522,37.6156',
  '...': '...'
}
EXAMPLE_RESPONSE_JSON = {
  'Moscow': (37, 23, '...'),
  'Another_city': ('another_temp')
}

CITIES = {
  'Moscow': '55.7522,37.6156',
  'Ufa': '54.7431,55.9678',
  'St-Petersburg': '59.9386,30.3141'
}