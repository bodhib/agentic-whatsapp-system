import os
import shutil

WHATSAPP_EXPORT_FOLDER = (
    "data/whatsapp_export"
)

IMAGES_FOLDER = "data/images"


def move_whatsapp_images():
    """
    Move WhatsApp images from export
    folder to images folder.
    """

    os.makedirs(
        IMAGES_FOLDER,
        exist_ok=True
    )

    moved_files = []

    for file_name in os.listdir(
        WHATSAPP_EXPORT_FOLDER
    ):

        source_path = os.path.join(
            WHATSAPP_EXPORT_FOLDER,
            file_name
        )

        # Skip chat.txt
        if file_name.endswith(".txt"):
            continue

        # Process only image files
        if file_name.lower().endswith(
            (
                ".jpg",
                ".jpeg",
                ".png",
                ".webp"
            )
        ):

            destination_path = os.path.join(
                IMAGES_FOLDER,
                file_name
            )

            shutil.copy(
                source_path,
                destination_path
            )

            moved_files.append(file_name)

    print(
        f"✅ Moved {len(moved_files)} images"
    )

    return moved_files