from crewai.tools import tool
from core.vision_service import match_product_service

import sys

@tool
def match_product(image_name: str):
    """
    Tool to match image with catalog using AI.
    """
    # print(f"🔍 Matching product for image: {image_name}")
    # sys.exit(0)

    return match_product_service(image_name)