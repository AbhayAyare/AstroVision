from PIL import Image
import os

def is_valid_image(file_path):
    try:
        img = Image.open(file_path)
        img.verify()
        return True
    except Exception:
        return False

dataset_path = "data/images"  # Update if path differs

bad_files = []

for root, dirs, files in os.walk(dataset_path):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            file_path = os.path.join(root, file)
            if not is_valid_image(file_path):
                bad_files.append(file_path)

print(f"Found {len(bad_files)} corrupted files.")

for bad in bad_files:
    os.remove(bad)
    print(f"Deleted: {bad}")

print("Dataset cleaned!")
