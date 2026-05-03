from crewai.tools import tool
from core.parser_service import parse_orders_service

import sys


@tool
def parse_orders(chat_path: str):
    """
    Tool to parse WhatsApp chat and extract structured orders.
    """
    # print(chat_path)
    # sys.exit(0)

    return parse_orders_service(chat_path)