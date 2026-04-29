import re

def order_lookup(text):
    match = re.search(r"\d+", text)

    return {
        "name": "order_lookup",
        "args": {
            "order_id": match.group() if match else None
        }
    } if match else None