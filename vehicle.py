from ultralytics import YOLO
import cv2
import numpy as np
from sort import Sort  # tracking library

# Load YOLOv8 model
model = YOLO("yolov8n.pt")
tracker = Sort()

vehicle_classes = ['car', 'bus', 'truck', 'motorbike']

# Choose source (0 = webcam or 'traffic.mp4')
cap = cv2.VideoCapture('sample.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO
    results = model(frame, verbose=False)
    detections = []

    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        if label in vehicle_classes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            detections.append([x1, y1, x2, y2, float(box.conf[0])])

    # 🧠 Safe SORT update
    if len(detections) > 0:
        tracked_objects = tracker.update(np.array(detections))
    else:
        tracked_objects = []

    count = len(tracked_objects)

    for obj in tracked_objects:
        x1, y1, x2, y2, obj_id = map(int, obj)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"ID {obj_id}", (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.putText(frame, f"Vehicles: {count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.imshow("Traffic Monitoring", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
