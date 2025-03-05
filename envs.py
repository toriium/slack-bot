import os
from pathlib import Path

from dotenv import find_dotenv, load_dotenv


ENV_PATH = os.path.dirname(os.path.realpath(__file__))
ENV_PATH = Path(ENV_PATH + '/env.env')

env_path = find_dotenv(ENV_PATH)
load_dotenv(env_path)


class Settings:
    SLACK_WEBHOOK_URL= os.getenv('SLACK_WEBHOOK_URL')
    SLACK_BOT_TOKEN= os.getenv('SLACK_BOT_TOKEN')
    SLACK_USER = os.getenv('SLACK_USER')



# CHANNEL = "#programming"
CHANNEL = "C03L0LPBYD9"
