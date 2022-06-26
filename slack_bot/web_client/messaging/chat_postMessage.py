from slack_sdk import WebClient

from envs import ENV, CHANNEL

client = WebClient(token=ENV.SLACK_BOT_TOKEN)

response = client.chat_postMessage(channel=CHANNEL,
                                   text="Sending a normal chat menssage")

ts = response['ts']

response = client.chat_postMessage(channel=CHANNEL,
                                   text="Repliplyng chat menssage",
                                   thread_ts=ts)

response = client.chat_postMessage(channel=CHANNEL,
                                   text="Repliplyng chat menssage with: 'replied to a thread'",
                                   thread_ts=ts,
                                   reply_broadcast=True)
