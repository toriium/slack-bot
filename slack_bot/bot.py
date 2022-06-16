from slack_sdk.webhook import WebhookClient

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

webhook_client = WebhookClient(url=SLACK_WEBHOOK_URL)

webhook_client.send(text=f'@here \n ola mundo')
