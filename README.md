# Hand Gesture Volume Control

![Demo](/images/output.gif) 

A Python project that uses hand gestures to control the system volume. It uses **Mediapipe** for hand tracking and **OpenCV** for real-time video processing.

---

## Features

- **Real-time Hand Tracking**: Detects hand landmarks.
- **Volume Control**: Adjusts volume based on the distance between the thumb and index finger.
- **Thumbs Up/Down Gestures**:
  - **Thumbs Up**: Pauses volume control.
  - **Thumbs Down**: Resumes volume control after 3 seconds.

---

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- Mediapipe (`mediapipe`)
- NumPy (`numpy`)
- Pycaw (`pycaw`)
- Comtypes (`comtypes`)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/hand-gesture-volume-control.git
   cd hand-gesture-volume-control

---

# MediaPipe Documentation

![MediaPipe](/images/ZnWo3pbWFbowexPE_image-58-.avif)

## Overview:
MediaPipe is a framework developed by Google for building multimodal applied machine learning pipelines. It provides tools for processing various types of data, including video, audio, and sensor data, and is commonly used for tasks like hand tracking, face detection, and pose estimation.

## Key Features:
- **Cross-Platform**: Works on multiple platforms including Android, iOS, and desktop.
- **Pre-built Solutions**: Offers pre-built solutions for tasks like hand tracking, face detection, and object detection.
- **Customizable Pipelines**: Allows developers to create custom pipelines for specific applications.
- **Real-Time Processing**: Designed for real-time performance, making it suitable for interactive applications.

## Common Use Cases:
- **Hand Tracking**: Detecting and tracking hand landmarks for gesture recognition.
- **Face Detection**: Identifying and tracking faces in images or video streams.
- **Pose Estimation**: Estimating human body poses from images or videos.
- **Object Detection**: Detecting objects within a video or image.

MediaPipe is widely used in applications requiring real-time, multimodal data processing, such as augmented reality, virtual reality, and interactive systems.

---

# Gesture Controls Documentation

![Gesture Controls](/images/figure6.png)

## General Gesture Controls:
- **Up**: Move or gesture upwards.
- **Down**: Move or gesture downwards.
- **Back**: Go back or return to a previous state.
- **Go forward**: Move forward or proceed to the next state.
- **Land**: Likely refers to a landing or neutral position.

## Right Hand-Specific Controls:
- **Right: Down**: Gesture with the right hand to move or indicate downward.
- **Right: Back**: Gesture with the right hand to go back.
- **Right: Forward**: Gesture with the right hand to move forward.
- **Right: OK**: Gesture with the right hand to confirm or approve.

## Additional Controls:
- **Stop**: Halt or stop the current action.
- **Left**: Move or gesture to the left.
- **Right: Stop**: Gesture with the right hand to stop.
- **Right: Left**: Gesture with the right hand to move left.
- **Right: Right**: Gesture with the right hand to move right.

These controls are part of a gesture-based interface, where hand movements or positions are used to perform specific actions or commands. The "Right" prefix indicates that these gestures are performed using the right hand.

---

# Hand Landmarks Documentation

![Hand Landmarks](/images/hand_landmarks_docs.png)

## Overview:
The hand landmarks image provides a visual representation of the key points detected on a human hand. These landmarks are used in applications like gesture recognition, hand tracking, and augmented reality.

## Key Points:
- **Wrist**: The base of the hand.
- **Thumb**: Includes landmarks for the carpometacarpal joint (CMC), metacarpophalangeal joint (MCP), interphalangeal joint (IP), and the tip (TIP).
- **Index Finger**: Includes landmarks for the metacarpophalangeal joint (MCP), proximal interphalangeal joint (PIP), distal interphalangeal joint (DIP), and the tip (TIP).
- **Middle Finger**: Includes landmarks for the metacarpophalangeal joint (MCP), proximal interphalangeal joint (PIP), distal interphalangeal joint (DIP), and the tip (TIP).
- **Ring Finger**: Includes landmarks for the metacarpophalangeal joint (MCP), proximal interphalangeal joint (PIP), distal interphalangeal joint (DIP), and the tip (TIP).
- **Pinky**: Includes landmarks for the metacarpophalangeal joint (MCP), proximal interphalangeal joint (PIP), distal interphalangeal joint (DIP), and the tip (TIP).

## Applications:
- **Gesture Recognition**: Identifying specific hand gestures for controlling devices or applications.
- **Hand Tracking**: Tracking the movement and position of the hand in real-time.
- **Augmented Reality**: Enhancing AR experiences by integrating hand movements and gestures.

This documentation is essential for developers working on applications that require precise hand tracking and gesture recognition.