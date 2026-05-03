from crewai.tools import tool
import os, sys
from core.media_handler import extract_image_names, move_images


@tool
def ingest_whatsapp_data(export_folder: str) -> str:
    """
    Load WhatsApp export data and move image files into the system image directory.

    Args:
        export_folder (str): Path to WhatsApp export folder containing chat.txt and media files.

    Returns:
        str: Summary of number of images processed.
    """
    chat_file = os.path.join(export_folder, "chat.txt")
    # print(chat_file)
    # sys.exit(0)

    images_folder = "data/images"

    os.makedirs(images_folder, exist_ok=True)

    image_names = extract_image_names(chat_file)
    moved_files = move_images(export_folder, images_folder, image_names)
    # print(f"{len(moved_files)} images ingested")
    # sys.exit(0)

    return f"{len(moved_files)} images ingested"