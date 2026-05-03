import uuid
from datetime import datetime
import os
import shutil


def create_order_service(order_data: dict):
    """
    Core service to create structured order and store image.
    """
    if order_data.get("status") != "matched":
        return {"status": "skipped"}

    order_id = str(uuid.uuid4())[:8]
    timestamp = str(datetime.now())

    src = os.path.join("data/images", order_data["image"])

    order_folder = f"data/order_images/order_{order_id}"
    os.makedirs(order_folder, exist_ok=True)

    dest = os.path.join(order_folder, order_data["image"])
    shutil.copy(src, dest)

    return {
        "order_id": order_id,
        "timestamp": timestamp,
        "product": order_data["product"],
        "price": order_data["price"],
        "image_path": dest
    }