from ultralytics import YOLO

# Load the 20-epoch trained model
model = YOLO(
    "runs/detect/runs/retail_yolo_20epochs/weights/best.pt"
)

# Test on new images
results = model.predict(
    source="test_images",
    conf=0.25,
    save=True
)

print("Prediction completed!")