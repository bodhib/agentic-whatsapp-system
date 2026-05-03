from crewai.tools import tool
from core.reporting_service import generate_report_service


@tool
def generate_report(orders: list):
    """
    Tool to generate Excel reports.
    """
    return generate_report_service(orders)