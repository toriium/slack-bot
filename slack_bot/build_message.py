import json
from datetime import datetime, timezone

from blockkit import Divider, Message, Section

from slack_bot.channels import TEST_CHANNEL

error_list = [
    {
        "client_id": 1,
        "error_message": "error_message 11111"
    },
    {
        "client_id": 2,
        "error_message": "error_message 222222"
    },
]


def create_error_section(client_id: str, error_message: str):
    error_block = []

    error_message = f"""
    *client_id*: {client_id} 
    Error message: 
    {error_message}
    """.strip()
    error_block.append(Section(text=error_message))
    error_block.append(Divider())

    return error_block


def main():
    # Base Block
    block_name = "BLOCK_NAME: [Crawlers Status]"
    base_blocks = [
        Section(text=block_name),
        Section(text=f"Generated At: {datetime.now()}"),
        Divider(),
    ]

    error_block = []
    for error in error_list:
        blocks = create_error_section(client_id=error["client_id"],error_message= error["error_message"])
        error_block.extend(blocks)

    message = Message(
        blocks=[
            *base_blocks,
            *error_block
        ]
    )

    blocks_payload = message.build()["blocks"]

    now = datetime.now(timezone.utc)
    start_of_day = datetime(now.year, now.month, now.day, tzinfo=timezone.utc).timestamp()

    ts_old = TEST_CHANNEL.get_target_message(target_text=block_name, oldest_ts=start_of_day)
    if ts_old:
        TEST_CHANNEL.delete_message(ts=ts_old)

    TEST_CHANNEL.post_message(blocks=blocks_payload)


if __name__ == '__main__':
    main()
