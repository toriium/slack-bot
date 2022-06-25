from pydantic import BaseSettings


class Settings(BaseSettings):
    SLACK_WEBHOOK_URL: str
    SLACK_BOT_TOKEN: str

    class Config:
        env_file = '../env.env'
        env_file_encoding = 'utf-8'


ENV = Settings()
