import os
from dotenv import load_dotenv

load_dotenv()


BROCKER_HOST=os.environ.get('BROCKER_HOST')
BROCKER_PORT=os.environ.get('BROCKER_PORT')

redis_url = f'redis://{BROCKER_HOST}:{BROCKER_PORT}/0'