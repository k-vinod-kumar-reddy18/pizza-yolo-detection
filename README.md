# Pizza Detection using YOLO

This project detects and classifies different types of pizza using YOLO.

## Pizza Classes

- Bianca
- Hawaiian
- Manager Choice
- Pepperoni

## Dataset

- Total Images: 400
- Training: 280
- Validation: 80
- Testing: 40

## Model

- YOLO26n
- Epochs: 20
- Batch Size: 2
- Image Size: 320
- Device: CPU

## Results

- Precision: 36.2%
- Recall: 66.0%
- mAP50: 44.1%
- mAP50-95: 40.2%

## ONNX Model Conversion

The trained YOLO model was converted from PyTorch format (`.pt`) to ONNX format (`.onnx`) for deployment and inference.

### Model Conversion

    from ultralytics import YOLO

    model = YOLO("best.pt")
    model.export(format="onnx")

The converted model is:

`best.onnx`

The ONNX model was successfully loaded and tested using ONNX Runtime.

### ONNX Inference

The exported ONNX model was used to perform inference on test images.

Example:

    from ultralytics import YOLO

    model = YOLO("best.onnx")
    results = model("test_images/piz2.jpg", imgsz=320, save=True)

The ONNX model successfully detected pizza classes such as:

- Hawaiian
- Bianca
- Pepperoni

## Files

- `combine_data.py` – Combines the dataset
- `split_data.py` – Splits data into train, validation and test
- `train.py` – Trains the YOLO model
- `predict.py` – Tests the trained model
- `data.yaml` – Dataset configuration

## Technologies

Python, YOLO, Ultralytics, ONNX, ONNX Runtime