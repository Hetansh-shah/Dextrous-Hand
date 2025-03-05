# Robotic Hand Control using MediaPipe & Modbus RTU 🤖🖐️
This project enables a robotic hand to mimic real-time human hand movements using MediaPipe for hand tracking and Modbus RTU for communication. The system captures hand gestures, processes the data, and sends precise motor commands to control the robotic fingers.

## Features
✅ Real-time hand tracking using MediaPipe
✅ Serial communication via UART + Modbus RTU
✅ Gesture-based robotic control with precise motor actuation
✅ CRC16 checksum for data integrity
✅ Python-powered automation for smooth execution

# Technologies Used
Python (serial, crcmod, mediapipe, struct, keyboard)
Modbus RTU Protocol for communication
MediaPipe for hand gesture recognition
# How It Works
MediaPipe detects real-time hand gestures.
The system maps finger positions to predefined robotic hand angles.
Modbus RTU commands are generated and sent via serial communication.
The robotic hand mirrors the detected gestures dynamically.
# Setup & Usage
Install dependencies:
  pip install serial crcmod mediapipe keyboard
Connect the robotic hand to the system via UART (COM port).
Run the Python script to start real-time gesture mirroring.
# Future Enhancements
🔹 Improve gesture recognition accuracy
🔹 Implement machine learning for adaptive movements
🔹 Add more predefined robotic hand gestures
