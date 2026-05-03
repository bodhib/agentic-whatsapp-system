import os
from core.image_matcher import match_image, load_catalog_embeddings
from core.catalog_loader import load_catalog

import sys

catalog_df, price_map, product_map = load_catalog("data/catalog.csv")
catalog = load_catalog_embeddings("data/catalog")


def match_product_service(image_name: str):
    """
    Core service to match image with catalog using CLIP.
    Only high-confidence matches are returned.
    """
    image_path = os.path.join("data/images", image_name)
    # print(image_path)
    # sys.exit(0)

    if not os.path.exists(image_path):
        return {"status": "error"}

    product, score = match_image(image_path, catalog)

    if product is None or score < 0.90:
        return {"status": "rejected", "score": score}

    return {
        "status": "matched",
        "product": product_map.get(product, product),
        "price": price_map.get(product, 0),
        "score": score,
        "image": image_name
    }