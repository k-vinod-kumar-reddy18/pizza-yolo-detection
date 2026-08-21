from ultralytics import YOLO

# Load pretrained YOLO model
model = YOLO("yolo26n.pt")

# Train for 20 epochs
results = model.train(
    data="data.yaml",
    epochs=20,
    batch=2,
    imgsz=320,
    lr0=0.01,
    device="cpu",
    workers=0,
    project="runs",
    name="retail_yolo_20epochs"
)

print("Training completed!")