from ultralytics import YOLO

# Load YOLOv8 model (nano version – fastest)
model = YOLO("yolov8n.pt")

# Run detection on an image and save results automatically
results = model.predict(
    source=r"C:\Users\Spandana H\.cache\kagglehub\datasets\vivek603\vehicle-detection-sample-and-output-videos\versions\1\Sample.mp4",  # image URL or local path
    save=True,       # saves output with bounding boxes
    show=True        # optional: shows it in a window
)

print("✅ Detection done! Saved results in 'runs/detect/predict' folder.")
