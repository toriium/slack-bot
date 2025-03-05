from slack_sdk import WebClient

from envs import Settings, CHANNEL


WEB_CLIENT = WebClient(token=Settings.SLACK_BOT_TOKEN)
