import os
import shutil
import re


def extract_image_names(chat_file):
    image_names = []

    pattern = r"(\w+\.PNG)" 

    with open(chat_file, "r", encoding="utf-8") as f:
        for line in f:
            matches = re.findall(pattern, line)
            image_names.extend(matches)

    return list(set(image_names))  # remove duplicates


def move_images(export_folder, destination_folder, image_names):
    os.makedirs(destination_folder, exist_ok=True)

    moved_files = []

    for root, _, files in os.walk(export_folder):
        for file in files:
            if file in image_names:
                src_path = os.path.join(root, file)
                dest_path = os.path.join(destination_folder, file)
                
                if not os.path.exists(dest_path):
                    shutil.copy(src_path, dest_path)
                    moved_files.append(file)

    print(f"📦 Moved {len(moved_files)} images")
    return moved_files