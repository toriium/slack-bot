from slack_sdk import WebClient

from envs import CHANNEL
from slack_bot.client import WEB_CLIENT


class Channel:

    def __init__(self, client: WebClient, channel_id: str):
        self.client = client
        self.channel_id = channel_id

    def get_target_message(self, target_text: str, oldest_ts: str):
        response = self.client.conversations_history(channel=self.channel_id, oldest=oldest_ts)
        messages = response["messages"]

        target_message = None
        for msg in messages:
            if "bot_id" in msg and target_text in msg.get("text"):
                target_message = msg

        if target_message:
            ts = target_message['ts']
            return ts

        return None

    def delete_message(self, ts: str):
        response = self.client.chat_delete(channel=self.channel_id, ts=ts)
        return response

    def post_message(self, text: str = None, blocks: dict = None):
        response = self.client.chat_postMessage(channel=self.channel_id, text=text, blocks=blocks)
        return response

    def update(self, ts: str, blocks: dict):
        response = self.client.chat_update(channel=self.channel_id, ts=ts, blocks=blocks)
        return response


TEST_CHANNEL = Channel(client=WEB_CLIENT, channel_id=CHANNEL)