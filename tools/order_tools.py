# =========================================
# FILE: tools/order_tools.py
# =========================================

from crewai.tools import tool

from core.parser_service import parse_orders_service
from core.vision_service import match_product_service
from core.order_service import create_order_service
from core.reporting_service import generate_report_service

import sys

# Global memory for lightweight workflow state
workflow_state = {}


@tool("Parse WhatsApp Orders")
def parse_orders_tool():
    """
    Parse WhatsApp chat export and extract orders.
    """
    
    orders = parse_orders_service(
        "data/whatsapp_export/chat.txt"
    )
    # print(orders)
    # sys.exit(0)
    workflow_state["orders"] = orders

    return f"Parsed {len(orders)} orders."


@tool("Match Product Images")
def match_products_tool():
    """
    Match customer images with catalog products.
    """

    orders = workflow_state.get("orders", [])

    final_orders = []

    for order in orders:

        if not order.get("image"):
            continue

        match_result = match_product_service(
            order["image"]
        )

        combined = {
            **order,
            **match_result
        }

        final = create_order_service(
            combined
        )

        if final.get("status") != "skipped":
            final_orders.append(final)

    workflow_state["final_orders"] = final_orders

    return (
        f"Processed {len(final_orders)} "
        f"matched orders."
    )


@tool("Generate Reports")
def generate_reports_tool():
    """
    Generate analytics and Excel reports.
    """

    final_orders = workflow_state.get(
        "final_orders",
        []
    )

    generate_report_service(final_orders)

    return "Reports generated successfully."