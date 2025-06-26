# 🌌 AstroVision: AI-Powered Stargazing Assistant

AstroVision is a real-time AI-powered constellation recognition app built for desktop using Python. It uses machine learning and computer vision to detect constellations from a live camera feed or uploaded images.

> 🔭 A perfect blend of astronomy, AI, and education!

---

## 📸 Screenshot

> 🖼️ Interface with webcam + upload functionality:

![AstroVision Screenshot](screenshots/app_ui.png) <!-- Save your screenshot as screenshots/app_ui.png -->

---

## 🛠 Features

- ✅ Real-time webcam-based constellation detection
- 🖼 Upload image for constellation prediction
- 📚 Built-in quiz mode for learning
- 🔁 Smoothing filter for stable real-time prediction
- 🌌 Dataset support for 88 constellations
- ☁️ (Optional) Firebase integration for logging

---

## 📁 Project Structure

AstroVision/
├── app.py # Main desktop UI app (Tkinter + OpenCV)
├── requirements.txt # All dependencies
├── firebase_config.json # Firebase key (optional)
│
├── model/
│ ├── train_model.py # Training script
│ └── constellation_model.h5 # Saved model (after training)
│
├── utils/
│ └── vision.py # Live prediction logic
│
├── data/
│ └── images/ # Dataset (constellation folders inside)
│ ├── Orion/
│ ├── UrsaMajor/
│ └── Cassiopeia/
│
├── quizzes/
│ └── questions.json # Astronomy quiz questions
├── clean_dataset.py # Fix corrupted images
├── README.md # This file
├── screenshots/
│ └── app_ui.png # UI image

Dataset Notes
Store images in data/images/<ConstellationName>/ format

At least 10+ images per class recommended

Can use image scraping tools or APIs to expand dataset

📚 Quiz Mode
A simple quiz UI pulls questions from quizzes/questions.json.
It opens a Tkinter input dialog for each question and scores your answers.


📦 Dependencies
txt
Copy
Edit
tensorflow
opencv-python
pillow
numpy
firebase-admin
