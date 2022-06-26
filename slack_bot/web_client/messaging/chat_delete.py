import time

from slack_sdk import WebClient

from envs import ENV, CHANNEL

client = WebClient(token=ENV.SLACK_BOT_TOKEN)

response = client.chat_postMessage(channel=CHANNEL,
                                   text="Sending a chat to be deleted")

ts = response['ts']

time.sleep(2)
response = client.chat_delete(channel=CHANNEL,
                              ts=ts, )
