from crewai.tools import tool
from core.order_service import create_order_service


@tool
def create_order(order_data: dict):
    """
    Tool to create structured order.
    """
    return create_order_service(order_data)