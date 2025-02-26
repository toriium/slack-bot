from slack_sdk import WebClient

from envs import ENV, CHANNEL


WEB_CLIENT = WebClient(token=ENV.SLACK_BOT_TOKEN)
