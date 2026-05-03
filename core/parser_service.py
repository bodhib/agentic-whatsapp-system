from core.parser import parse_chat
from core.extractor import extract_orders

import sys


def parse_orders_service(chat_path: str):
    """
    Core service to parse WhatsApp chat and extract structured orders.
    """
    df = parse_chat(chat_path)
    orders = extract_orders(df)
    # print(f"Extracted {len(orders)} orders from chat")
    # sys.exit(0)

    return orders.to_dict(orient="records")