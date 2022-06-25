from slack_sdk.webhook import WebhookClient

from envs import SLACK_WEBHOOK_URL

webhook_client = WebhookClient(url=SLACK_WEBHOOK_URL)
webhook_client.send(text=f'@here \n ola mundo')
