# Hand Gesture Volume Control

![Demo](/images/output.gif) <!-- Add a demo GIF or video here -->

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