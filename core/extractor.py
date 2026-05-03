import re
import pandas as pd

import sys

def extract_orders(df):
    orders = []

    for _, row in df.iterrows():
        message = row["message"]
        
        # detect quantity
        qty_match = re.search(r"\d+", message)
        quantity = int(qty_match.group()) if qty_match else 1

        # detect if image reference exists
        match = re.search(r"image:\s*(\S+)", message)
        image_name = match.group(1) if match else None

        orders.append({
            "date": row["date"],
            "customer": row["customer"],
            "quantity": quantity,
            "image": image_name
        })
    
    return pd.DataFrame(orders)