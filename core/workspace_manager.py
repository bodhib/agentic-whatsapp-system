import shutil
import os


def reset_workspace():
    """
    Reset temporary runtime folders.
    """

    folders = [
        "data/whatsapp_export",
        "data/images"
    ]

    for folder in folders:

        shutil.rmtree(
            folder,
            ignore_errors=True
        )

        os.makedirs(
            folder,
            exist_ok=True
        )

    print("✅ Workspace reset")