import json

from blockkit import Divider, Message, Section

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
    base_header = [
        Section(text="Crawlers Logs"),
        Divider(),
    ]

    error_block = []
    for error in error_list:
        blocks = create_error_section(client_id=error["client_id"],error_message= error["error_message"])
        error_block.extend(blocks)


    payload = Message(
        blocks=[
            *base_header,
            *error_block
        ]
    ).build()

    json_str = json.dumps(payload)
    print(json_str)


if __name__ == '__main__':
    main()
