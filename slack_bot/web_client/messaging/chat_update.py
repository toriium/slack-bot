import time

from slack_sdk import WebClient

from envs import ENV, CHANNEL

client = WebClient(token=ENV.SLACK_BOT_TOKEN)

response = client.chat_postMessage(channel=CHANNEL,
                                   text="Sending a chat to be updated")

ts = response['ts']

time.sleep(2)
response = client.chat_update(channel=CHANNEL,
                              ts=ts,
                              text="updated chat"
                              )
