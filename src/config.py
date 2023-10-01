import os
from dotenv import load_dotenv

load_dotenv()


BROCKER_USER=os.environ.get('BROCKER_USER')
BROCKER_PASSWORD=os.environ.get('BROCKER_PASSWORD')
BROCKER_HOST=os.environ.get('BROCKER_HOST')
BROCKER_PORT=os.environ.get('BROCKER_PORT')
BROCKER_VHOST=os.environ.get('BROCKER_VHOST')

# broker_url = f'amqp://{BROCKER_USER}:{BROCKER_PASSWORD}@{BROCKER_HOST}:{BROCKER_PORT}/{BROCKER_VHOST}'

redis_url = f'redis://{BROCKER_HOST}:{BROCKER_PORT}/0'