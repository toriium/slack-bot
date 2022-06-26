import logging

# logging.basicConfig(level=logging.DEBUG)


response = client.chat_postEphemeral(
    channel=channel,
    text="Chat menssage to a specific person",
    user=ENV.SLACK_PERSONAL_USER
)

response = client.chat_postMessage(
    channel=channel,
    thread_ts="1476746830.000003",
    text="Chat menssage to a thread_ts",
    reply_broadcast=True
)

print('')
