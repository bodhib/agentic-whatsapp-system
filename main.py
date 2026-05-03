from core.parser_service import parse_orders_service
from core.vision_service import match_product_service
from core.order_service import create_order_service
from core.reporting_service import generate_report_service

from core.media_handler import extract_image_names, move_images

import os
import sys

def run():

    EXPORT_FOLDER = "data/whatsapp_export"
    CHAT_FILE = os.path.join(EXPORT_FOLDER, "chat.txt")
    IMAGES_FOLDER = "data/images"

    # Step 0: Extract and move images
    image_names = extract_image_names(CHAT_FILE)
    # print(image_names)
    # sys.exit()
    move_images(EXPORT_FOLDER, IMAGES_FOLDER, image_names)

    orders = parse_orders_service("data/whatsapp_export/chat.txt")
    # print(orders)
    # sys.exit(0)

    final_orders = []

    for order in orders:
        if not order.get("image"):
            continue

        match_result = match_product_service(order["image"])
        # print(match_result)
        # sys.exit(0)

        combined = {**order, **match_result}

        final = create_order_service(combined)

        if final.get("status") != "skipped":
            final_orders.append(final)

    # print(final_orders)
    # sys.exit(0)

    generate_report_service(final_orders)

    print("✅ Pipeline completed successfully!")


if __name__ == "__main__":
    run()