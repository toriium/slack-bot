from slack_sdk.webhook import WebhookClient

from envs import ENV

webhook_client = WebhookClient(url=ENV.SLACK_WEBHOOK_URL)
webhook_client.send(text=f'@here \n ola mundo')
