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

## Files

- `combine_data.py` – Combines the dataset
- `split_data.py` – Splits data into train, validation and test
- `train.py` – Trains the YOLO model
- `predict.py` – Tests the trained model
- `data.yaml` – Dataset configuration

## Technologies

Python, YOLO, Ultralytics
