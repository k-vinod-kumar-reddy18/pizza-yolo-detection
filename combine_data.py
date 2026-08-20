import os
import shutil

# Original folders
classes = [
    "binca",
    "hawaini",
    "managerchoice",
    "pepporni"
]

# Combined dataset folder
output = "combined_data"

# Create combined folders
os.makedirs(f"{output}/images", exist_ok=True)
os.makedirs(f"{output}/labels", exist_ok=True)

total_images = 0
total_labels = 0

# Process each class folder
for class_name in classes:

    image_folder = f"{class_name}/images/train"
    label_folder = f"{class_name}/labels/train"

    print(f"\nProcessing: {class_name}")

    for image_name in os.listdir(image_folder):

        if not image_name.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        image_path = os.path.join(image_folder, image_name)

        label_name = os.path.splitext(image_name)[0] + ".txt"
        label_path = os.path.join(label_folder, label_name)

        # Make sure annotation exists
        if not os.path.exists(label_path):
            print("Missing label:", image_name)
            continue

        # Prevent duplicate filenames
        new_image_name = f"{class_name}_{image_name}"
        new_label_name = f"{class_name}_{label_name}"

        # Copy image
        shutil.copy2(
            image_path,
            os.path.join(output, "images", new_image_name)
        )

        # Copy label
        shutil.copy2(
            label_path,
            os.path.join(output, "labels", new_label_name)
        )

        total_images += 1
        total_labels += 1

print("\n----------------------------")
print("COMBINATION COMPLETED")
print("----------------------------")
print("Total images:", total_images)
print("Total labels:", total_labels)

if total_images == 400 and total_labels == 400:
    print("SUCCESS: Exactly 400 images and 400 labels copied.")
else:
    print("WARNING: Expected 400 images and 400 labels.")
