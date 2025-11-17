🚗 Vehicle Detection & Counting using YOLOv8 + SORT Tracker
---------------------------------------------------------------
A real-time traffic monitoring system that detects, tracks, and counts moving vehicles from video streams using YOLOv8 Object Detection and SORT Tracking Algorithm.
This project helps improve traffic analysis, congestion monitoring, and automated traffic rule enforcement.
---------------------------------------------------------------
📝 Abstract
Urban traffic congestion is a major challenge in modern cities. Manual counting and monitoring are inefficient and prone to human error.
This project proposes an automated vehicle detection and counting system using YOLOv8, a state-of-the-art object detection model, combined with SORT, a lightweight and fast tracking algorithm.
The system processes traffic video streams, identifies different vehicle classes, counts unique vehicles, and reduces duplicate counting using tracking IDs.
----------------------------------------------------------------
🎯 Objectives
1. Detect vehicles (car, bus, truck, motorbike) using YOLOv8
2. Assign unique IDs to each vehicle using SORT tracking
3. Count vehicles passing through the frame
4. Support real-time video streams and CCTV footage
5. Provide accurate, stable counting even in dense traffic
----------------------------------------------------------------
🛠️ Tools & Technologies Used
Component	Description
Python 3.10	Programming language
YOLOv8 (Ultralytics)	Vehicle detection
SORT Tracker	Tracks vehicles using Kalman Filter + IoU
OpenCV	Video frame processing
NumPy	Numerical operations
Jupyter Notebook / VS Code	Code development
CUDA GPU	Accelerated model inference
---------------------------------------------------------------
🧠 Methodology
The system works in the following stages:
1. Input Video:
Live webcam feed
CCTV/traffic video
MP4/MOV video files
2. YOLOv8 Object Detection
YOLO processes each frame and identifies vehicles with bounding boxes.
Classes detected:
Car
Bus
Truck
Motorbike
3. SORT Tracking
SORT assigns a unique ID to every detected vehicle using:
Kalman filter prediction
IoU matching between frames
This prevents double counting.
4. Vehicle Counting Logic
Every unique ID is added to a “counted set” only once.
5. Display & Output
Bounding boxes
-------------------------------------------------------------------
Class names

Unique ID per vehicle
