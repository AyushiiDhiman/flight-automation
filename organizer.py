import os
import shutil
from utils.logger import get_logger

logger = get_logger("file-automation")

SOURCE_FOLDER = "data"
TARGET_FOLDERS = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Others": []
}

for folder in TARGET_FOLDERS.keys():
    os.makedirs(folder, exist_ok=True)

def organize_files():
    logger.info(f"Organizing files from '{SOURCE_FOLDER}'...")
    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)
        if os.path.isfile(file_path):
            moved = False
            for folder, exts in TARGET_FOLDERS.items():
                if any(file.lower().endswith(ext) for ext in exts):
                    shutil.move(file_path, os.path.join(folder, file))
                    logger.info(f"{file} moved to {folder}")
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join("Others", file))
                logger.info(f"{file} moved to Others")
    logger.info("File organization complete!")

if __name__ == "__main__":
    organize_files()
