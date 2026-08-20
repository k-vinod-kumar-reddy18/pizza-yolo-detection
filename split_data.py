import os
import shutil
import random

# Combined data
IMAGE_SOURCE = "combined_data/images"
LABEL_SOURCE = "combined_data/labels"

# Final dataset
OUTPUT = "dataset"

# Create folders
for split in ["train", "val", "test"]:
    os.makedirs(f"{OUTPUT}/images/{split}", exist_ok=True)
    os.makedirs(f"{OUTPUT}/labels/{split}", exist_ok=True)

# Get all images
images = [
    file for file in os.listdir(IMAGE_SOURCE)
    if file.lower().endswith((".jpg", ".jpeg", ".png"))
]

print("Total images found:", len(images))

# Check exactly 400
if len(images) != 400:
    print("ERROR: Expected exactly 400 images.")
    print("Found:", len(images))
    exit()

# Shuffle images
random.seed(42)
random.shuffle(images)

# Calculate split
train_count = 280
val_count = 80
test_count = 40

train_images = images[:train_count]
val_images = images[train_count:train_count + val_count]
test_images = images[train_count + val_count:]

print("\nDataset split:")
print("Train:", len(train_images))
print("Validation:", len(val_images))
print("Test:", len(test_images))

# Copy function
def copy_files(image_list, split):

    for image_name in image_list:

        # Image path
        image_path = os.path.join(
            IMAGE_SOURCE,
            image_name
        )

        # Corresponding label
        label_name = os.path.splitext(image_name)[0] + ".txt"

        label_path = os.path.join(
            LABEL_SOURCE,
            label_name
        )

        # Check label
        if not os.path.exists(label_path):
            print("ERROR: Missing label:", label_name)
            continue

        # Copy image
        shutil.copy2(
            image_path,
            f"{OUTPUT}/images/{split}/{image_name}"
        )

        # Copy label
        shutil.copy2(
            label_path,
            f"{OUTPUT}/labels/{split}/{label_name}"
        )


# Copy data
copy_files(train_images, "train")
copy_files(val_images, "val")
copy_files(test_images, "test")

print("\n----------------------------")
print("DATASET SPLIT COMPLETED")
print("----------------------------")

print("Train:", len(os.listdir(f"{OUTPUT}/images/train")))
print("Validation:", len(os.listdir(f"{OUTPUT}/images/val")))
print("Test:", len(os.listdir(f"{OUTPUT}/images/test")))
