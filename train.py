from ultralytics import YOLO

model = YOLO("yolo26n.pt")

results = model.train(
    data="data.yaml",
    epochs=5,
    batch=2,
    imgsz=320,
    lr0=0.01,
    device="cpu",
    workers=0,
    project="runs",
    name="retail_yolo_initial"
)

print("Training completed!")