import pandas as pd

def load_catalog(csv_path):
    df = pd.read_csv(csv_path)

    # Convert to dictionary
    price_map = dict(zip(df["image"], df["price"]))
    product_map = dict(zip(df["image"], df["product"]))

    return df, price_map, product_map