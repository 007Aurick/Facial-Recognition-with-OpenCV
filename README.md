# 🧠 Real-Time Face Recognition System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)
![Face Recognition](https://img.shields.io/badge/FaceRecognition-AI-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

A real-time facial recognition system built with Python that detects and identifies faces from a live webcam feed using deep learning-based face embeddings.

---

## 🔥 Features

* 🎥 Real-time webcam face detection
* 🧠 Face recognition using 128-d facial embeddings
* 👥 Multi-person identification
* 🟩 Bounding box + name labeling
* ❓ Unknown face detection
* 📸 Screenshot capture (`s` key)
* 📊 Live FPS display

---

## ⚙️ Tech Stack

* Python 🐍
* OpenCV 🎥
* face_recognition 🤖
* NumPy 🔢

---

## 🧩 How It Works

* Load known images
* Convert faces → numerical encodings
* Capture webcam frames
* Detect faces in real time
* Compare encodings using distance metrics
* Return best match name

---

## 📁 Project Structure

```
project/
│
├── aurick.jpg
├── lebron.png
├── main.py
├── haarcascade_frontalface_default.xml (optional)
└── README.md
```

---

## 🚀 Installation

```bash
pip install opencv-python face-recognition numpy
```

⚠️ If `dlib` errors occur, install:

```bash
pip install cmake
pip install dlib
```

---

## ▶️ Run the Project

```bash
python main.py
```

### Controls:

* `q` → Quit program
* `s` → Save screenshot

---

## 🧠 Core Idea

This project uses **face embeddings**, not traditional image matching.

Each face is converted into a 128-dimensional vector and compared using distance similarity.

---

## 📌 Notes

* Works best with good lighting
* Frontal faces improve accuracy
* Performance depends on CPU speed
* Add multiple images per person for better results

---

## 🔮 Future Improvements

* 🔐 Face-based access control system
* 🗄️ Database storage for users
* 📈 Attendance tracking system
* 🎯 Face tracking (no flicker recognition)
* 🌐 Web dashboard (React UI)
* ⚡ FPS optimization (real-time boost)

---

## 👨‍💻 Author

Built as a computer vision + AI learning project.

---

## ⭐ If you like this project

Drop a ⭐ on the repo and keep building 🚀
