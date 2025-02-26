import time
from datetime import datetime, timezone

from slack_sdk import WebClient

from envs import ENV, CHANNEL
from slack_bot.client import WEB_CLIENT

now = datetime.now(timezone.utc)
start_of_day = datetime(now.year, now.month, now.day, tzinfo=timezone.utc).timestamp()

BASE_BLOCK = {
    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "plain_text",
                "emoji": True,
                "text": "Crawlers Logs"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "This is a mrkdwn section block :ghost: *this is bold*, and ~this is crossed out~, and <https://google.com|this is a link>"
            }
        }
    ]
}

response = WEB_CLIENT.conversations_history(channel=CHANNEL, oldest=start_of_day)
messages = response["messages"]

# Filter messages sent by the bot containing "this is the memo"
target_text = "Sending a normal chat menssage"
target_message = None
for msg in messages:
    if "bot_id" in msg and msg.get("text") == target_text:
        target_message = msg

ts = target_message['ts']
blocks = [
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "*Updated Memo:*\nThis is the updated memo."}
    }
]
WEB_CLIENT.chat_update(channel=CHANNEL, ts=ts, blocks=blocks)
print(f"Updated memo at {datetime.fromtimestamp(float(ts), tz=timezone.utc)}")
