import os
from pathlib import Path

from pydantic import BaseSettings

ENV_PATH = os.path.dirname(os.path.realpath(__file__))
ENV_PATH = Path(ENV_PATH + '/env.env')


class Settings(BaseSettings):
    SLACK_WEBHOOK_URL: str
    SLACK_BOT_TOKEN: str
    SLACK_USER: str

    class Config:
        env_file = ENV_PATH
        env_file_encoding = 'utf-8'


ENV = Settings()
# CHANNEL = "#programming"
CHANNEL = "C03L0LPBYD9"
