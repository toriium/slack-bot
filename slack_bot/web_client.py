import logging

from slack_sdk import WebClient

from envs import ENV

client = WebClient(token=ENV.SLACK_BOT_TOKEN)

response = client.chat_postMessage(
    channel="#programming",
    text="Hello from your app"
)
print('')
