from slack_sdk import WebClient

from envs import ENV, CHANNEL

client = WebClient(token=ENV.SLACK_BOT_TOKEN)

response = client.chat_postEphemeral(channel=CHANNEL,
                                     text="Chat menssage to a specific person",
                                     user=ENV.SLACK_USER, )
