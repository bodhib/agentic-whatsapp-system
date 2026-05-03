import pandas as pd
import os


def generate_report_service(orders: list):
    """
    Core service to generate Excel reports.
    """
    if not orders:
        return "No valid orders"

    os.makedirs("output", exist_ok=True)

    df = pd.DataFrame(orders)
    df["revenue"] = df["price"]

    df.to_excel("output/orders.xlsx", index=False)

    summary = df.groupby("product")["revenue"].sum().reset_index()
    summary.to_excel("output/report.xlsx", index=False)

    return "Reports generated"