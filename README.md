# 🧠 Alzheimer’s Detection with Generative AI

## 📌 Overview

This project focuses on detecting **Alzheimer’s Disease (AD)** using **Deep Learning** and enhancing the diagnostic experience with **Generative AI**. It combines medical image analysis and AI-driven interaction to support both patients and healthcare providers.

Alzheimer’s is a progressive neurodegenerative disorder that affects memory, thinking, and behavior. Early detection is crucial for slowing progression and improving patient care.

---

## 🎯 Objectives

* Develop a **deep learning model** to detect Alzheimer’s from medical images (MRI).
* Use **Generative AI** to:

  * Support diagnosis confirmation
  * Provide patient-friendly explanations
  * Reduce stress and anxiety
* Build an **interactive system** for both patients and doctors.

---

## 👥 Target Users

* Patients aged **50–85** (early & middle stages)
* Doctors and healthcare providers

---

## ⚙️ Features

### 🧪 Alzheimer’s Detection

* Upload MRI image
* Classify into 4 categories:

  * Alzheimer’s Disease
  * Cognitively Normal
  * Early Mild Cognitive Impairment
  * Late Mild Cognitive Impairment

### 🤖 AI Chatbot

* Answers patient questions
* Explains diagnosis and treatment
* Provides recommendations and guidance

### 💬 Doctor Communication

* Chat with doctors
* Book appointments
* Track medical history

### 📊 Reports & History

* Save test results
* View previous diagnoses

### 🗺️ Smart Map

* Find nearest doctors/hospitals
* Show distance and travel time

---

## 🧠 Models Used

### Image Classification Models

* CNN (Custom Model)
* VGG16
* DenseNet201
* ResNet152V2
* MobileNetV2

### NLP / Generative Models

* Transformer (custom)
* GPT-2 (fine-tuned)
* Autoencoder

---

## 📂 Dataset

* ~33,984 MRI images
* 4 classification categories
* Data split:

  * 80% Training
  * 10% Validation
  * 10% Testing

### Data Processing

* Preprocessing & normalization
* Data augmentation:

  * Rotation
  * Flipping
  * Zooming
  * Cropping

---

## 🏗️ System Architecture

The system includes:

* Frontend (User Interface)
* Backend (Flask)
* AI Models (DL + NLP)
* Database (Firebase / Local DB)

### Key Components

* Authentication system
* Image classification module
* Chatbot module
* Notification system

---

## 🛠️ Technologies Used

* Python
* TensorFlow / Keras
* Machine Learning & Deep Learning
* NLP & NLU
* Flask
* Firebase
* Mobile Development tools

---

## 📊 Evaluation Metrics

* Accuracy
* Confusion Matrix
* Classification Report
* Model comparison across architectures

---

## 🔒 Non-Functional Requirements

* Fast response time
* High reliability
* Scalability
* Data security (especially medical data)
* User-friendly interface

---

## 🚀 Future Work

* Improve model accuracy with larger datasets
* Deploy as a mobile/web application
* Integrate real-time hospital systems
* Enhance chatbot with more medical knowledge

---

## 📚 References

* TensorFlow
* Kaggle datasets
* ADNI dataset
* GPT-2 (OpenAI)
* Research papers on Transformers

---

## ❤️ Acknowledgment

Special thanks to supervisors, faculty, and everyone who contributed to the success of this project.

---
