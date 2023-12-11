from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOMORROWIO_TOKEN')

DEFAULT_CORDS = '55.7522,37.6156'

URL = 'https://api.tomorrow.io/v4/weather/forecast?location={cords}&timesteps=1d&apikey={TOKEN}'

EXAMPLE_DICT = {
  'Moscow': '55.7522,37.6156',
  '...': '...'
}
EXAMPLE_RESPONSE_JSON = {
  'Moscow': (37.)
}