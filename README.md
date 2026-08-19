# VisionVoice AI: Smart Assistant for the Visually Impaired

VisionVoice AI is an AI-based assistive system designed to help visually impaired users understand their surroundings through a combination of **Computer Vision and Voice Technology**.

The system can currently detect common objects using YOLO, identify objects through a live camera, and provide spoken descriptions. It also includes OCR functionality for detecting and reading text from images.

The project is being developed further to include **Indian currency recognition, voice commands, and a complete mobile application**.

---

## Features

### Currently Implemented

* Object detection using YOLO
* Live camera object detection
* Confidence-based detection filtering
* Text-to-Speech output
* Stable object detection before speaking
* OCR-based text recognition
* CPU-based AI processing
* Modular project structure

### Currently Under Development

* Indian currency recognition

  * ₹10
  * ₹20
  * ₹50
  * ₹100
  * ₹200
  * ₹500
* Custom YOLO training for Indian currency
* Voice commands
* Vision + Voice interaction
* Android application
* Improved accuracy and performance

---

# Technologies Used

| Technology  | Purpose                                   |
| ----------- | ----------------------------------------- |
| Python 3.13 | Main programming language                 |
| YOLO11      | Object detection                          |
| Ultralytics | YOLO implementation                       |
| OpenCV      | Camera and image processing               |
| EasyOCR     | Text recognition                          |
| PyTTSX3     | Text-to-Speech                            |
| PyTorch     | Deep learning framework used by AI models |
| VS Code     | Development environment                   |
| Git/GitHub  | Version control                           |

---

# System Requirements

### Hardware

* Windows laptop/PC
* Webcam or laptop camera
* Microphone
* Speakers/headphones
* Internet connection for initial package/model downloads

### Software

* Windows 10/11
* Python 3.13
* Visual Studio Code
* PowerShell or Command Prompt

---

# Project Structure

```text
Vision Voice AI/
│
├── images/
│   ├── test.jpg
│   └── text_test.jpg
│
├── models/
│
├── modules/
│   ├── object_detection.py
│   ├── ocr.py
│   └── speech.py
│
├── output/
│
├── currency_dataset/
│   ├── images/
│   │   ├── train/
│   │   ├── val/
│   │   └── test/
│   │
│   └── labels/
│       ├── train/
│       ├── val/
│       └── test/
│
├── venv/
│
├── camera_detection.py
├── main.py
├── requirements.txt
├── README.md
└── yolo11n.pt
```

> The `currency_dataset` folders are for the upcoming Indian currency recognition module. The custom currency model has not been trained yet.

---

# Installation

## 1. Install Python

Install Python 3.13 and verify:

```powershell
python --version
```

Expected:

```text
Python 3.13.x
```

Check pip:

```powershell
pip --version
```

---

# 2. Open the Project in VS Code

Open the project folder:

```text
Vision Voice AI
```

Open the VS Code terminal.

---

# 3. Create Virtual Environment

Run:

```powershell
py -3.13 -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\activate
```

After activation, the terminal should show:

```text
(venv) PS D:\...\Vision Voice AI>
```

Always make sure `(venv)` is visible before running the project.

---

# 4. Install Required Libraries

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install YOLO, OpenCV and Text-to-Speech:

```powershell
pip install ultralytics opencv-python pyttsx3
```

Install EasyOCR:

```powershell
pip install easyocr
```

Or install all saved dependencies:

```powershell
pip install -r requirements.txt
```

---

# 5. Verify Installation

### Check YOLO

```powershell
python -c "from ultralytics import YOLO; print('YOLO is working!')"
```

Expected:

```text
YOLO is working!
```

### Check OpenCV

```powershell
python -c "import cv2; print('OpenCV version:', cv2.__version__)"
```

### Check Text-to-Speech

```powershell
python -c "import pyttsx3; print('Text-to-Speech is working!')"
```

### Check EasyOCR

```powershell
python -c "import easyocr; print('EasyOCR is working!')"
```

---

# Object Detection

The project uses a pretrained YOLO11 model for general object detection.

The model can recognize common objects such as:

* Person
* Laptop
* Cell phone
* Bottle
* Chair
* Book
* Car
* Dog
* and other supported object classes

No custom training is currently required for general object detection.

---

# Run Image Object Detection

Place an image inside:

```text
images/test.jpg
```

Run:

```powershell
python modules/object_detection.py
```

The program will:

1. Load the pretrained YOLO model.
2. Analyze the image.
3. Detect objects.
4. Display bounding boxes.
5. Print detected objects and confidence scores.

Example:

```text
Detected Objects:

person (confidence: 0.86)
laptop (confidence: 0.75)
bottle (confidence: 0.73)
```

---

# Run Object Detection with Voice

The object detection module is connected with `speech.py`.

The system can produce a response such as:

```text
Assistant: I can see a person, laptop, bottle.
```

The response is also spoken through the computer's speakers.

---

# Live Camera Detection

The project can detect objects from a live webcam.

Run:

```powershell
python camera_detection.py
```

The camera window will open.

Point the camera toward an object.

For example:

```text
Person
Cell phone
Bottle
Laptop
```

YOLO will display bounding boxes and confidence values.

Press:

```text
Q
```

to close the camera.

---

# Camera Configuration

The current project uses the Windows DirectShow camera backend:

```python
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
```

If the camera cannot be opened, try another camera index:

```python
camera = cv2.VideoCapture(1, cv2.CAP_DSHOW)
```

Make sure other applications such as Zoom, Teams, Google Meet, or the Windows Camera application are not using the webcam.

---

# Voice Output

The project uses `pyttsx3` for local Text-to-Speech.

The `speech.py` module contains the speech function:

```python
speak("I can see a bottle.")
```

The computer will speak:

> I can see a bottle.

The project currently performs Text-to-Speech locally and does not require a paid API.

---

# OCR — Text Recognition

EasyOCR is used to detect text from images.

Place an image containing clear text inside:

```text
images/text_test.jpg
```

Update the image path in:

```text
modules/ocr.py
```

Then run:

```powershell
python modules/ocr.py
```

Example output:

```text
Detected Text:

VISIONVOICE AI
SMART ASSISTANT
FOR VISUALLY IMPAIRED
```

The OCR module is currently being tested separately. The next step is to connect OCR with Text-to-Speech.

---

# AI Architecture

The current system works approximately as follows:

```text
                    VisionVoice AI
                          |
              +-----------+-----------+
              |                       |
           Camera                   Image
              |                       |
              +-----------+-----------+
                          |
                     YOLO Model
                          |
                    Object Detection
                          |
                     Object Names
                          |
                    Text-to-Speech
                          |
                       Speaker
```

The OCR module works as:

```text
Image
  |
  ↓
EasyOCR
  |
Detected Text
  |
  ↓
Text-to-Speech
  |
  ↓
Speaker
```

---

# Indian Currency Recognition

Indian currency recognition is an important feature planned for the project.

The current pretrained YOLO model is not being relied upon for accurate denomination-specific recognition.

We will create a custom dataset containing:

```text
₹10
₹20
₹50
₹100
₹200
₹500
```

The planned custom model will learn to identify the denomination of an Indian currency note.

---

## Currency Dataset Plan

The initial dataset target is approximately:

```text
₹10   → 200 images
₹20   → 200 images
₹50   → 200 images
₹100  → 200 images
₹200  → 200 images
₹500  → 200 images
```

Total:

```text
Approximately 1200 images
```

Images should contain variations in:

* Lighting
* Camera angle
* Distance
* Background
* Orientation
* Position
* Hand-held notes
* Notes placed on surfaces
* Multiple notes
* Partially covered notes

The dataset will eventually be divided into:

```text
70% → Training
20% → Validation
10% → Testing
```

---

# Planned Currency AI Pipeline

```text
Camera
   |
   ↓
Currency Detection Model
   |
   ↓
Denomination
   |
   ├── ₹10
   ├── ₹20
   ├── ₹50
   ├── ₹100
   ├── ₹200
   └── ₹500
   |
   ↓
Text-to-Speech
   |
   ↓
"This is a 500 rupee note."
```

---

# Accuracy Improvement

The accuracy of the system will be improved through:

* Larger and more diverse datasets
* Proper image annotation
* Different lighting conditions
* Different camera angles
* Data augmentation
* Confidence threshold tuning
* Custom YOLO training
* Validation using unseen images
* Testing on real-world images
* Removing incorrect or poor-quality training samples

For the final evaluation, we plan to measure:

* Precision
* Recall
* mAP
* False positives
* False negatives
* Confusion matrix

---

# Current Development Status

| Module                          | Status         |
| ------------------------------- | -------------- |
| Python environment              | ✅ Completed    |
| Virtual environment             | ✅ Completed    |
| YOLO installation               | ✅ Completed    |
| General object detection        | ✅ Completed    |
| Image detection                 | ✅ Completed    |
| Live camera detection           | ✅ Completed    |
| Confidence filtering            | ✅ Completed    |
| Stable detection                | ✅ Completed    |
| Text-to-Speech                  | ✅ Completed    |
| YOLO + Voice integration        | ✅ Completed    |
| EasyOCR installation            | ✅ Completed    |
| OCR text detection              | ✅ Completed    |
| OCR + Voice                     | 🔄 Next        |
| Indian currency dataset         | 🔄 In progress |
| Currency annotation             | ⏳ Planned      |
| Custom currency training        | ⏳ Planned      |
| Currency accuracy evaluation    | ⏳ Planned      |
| Voice commands                  | ⏳ Planned      |
| Full Vision + Voice integration | ⏳ Planned      |
| Android application             | ⏳ Planned      |

---

# Important Notes

### Pretrained Model

The current general object detection uses a pretrained YOLO11 model.

We are **not training YOLO from scratch**.

Custom training will be used specifically for features such as Indian currency recognition.

### GPU

EasyOCR may display a message such as:

```text
Neither CUDA nor MPS are available - defaulting to CPU
```

This is not an error.

It means the model is running on the CPU instead of a supported GPU.

The project can still run.

### Internet

Internet is mainly required for:

* Installing Python packages
* Downloading model weights
* Initial AI model setup

The core object detection and Text-to-Speech components can run locally after installation.

---

# Running the Project

Make sure the virtual environment is active:

```powershell
.\venv\Scripts\activate
```

Then use the appropriate command.

### Test object detection:

```powershell
python modules/object_detection.py
```

### Test live camera:

```powershell
python camera_detection.py
```

### Test OCR:

```powershell
python modules/ocr.py
```

---

# Development Roadmap

```text
Phase 1
Environment Setup
        ↓
Phase 2
General Object Detection
        ↓
Phase 3
Live Camera
        ↓
Phase 4
Voice Output
        ↓
Phase 5
OCR
        ↓
Phase 6
Indian Currency Dataset
        ↓
Phase 7
Currency Annotation
        ↓
Phase 8
Custom YOLO Training
        ↓
Phase 9
Voice Commands
        ↓
Phase 10
Integrate All AI Modules
        ↓
Phase 11
Android Application
        ↓
Phase 12
Testing and Accuracy Evaluation
```

---

# Project Goal

The final goal of VisionVoice AI is to create an affordable and accessible assistant that combines **vision and voice** to help visually impaired users identify objects, recognize Indian currency, read text, and interact with their surroundings through spoken feedback.

The final system is intended to provide information in a simple, hands-free manner using a camera, microphone, AI models, and a speaker.

---

## Project Status

**Current stage:** AI prototype development

**Next major task:** Build and annotate the Indian currency dataset and train a custom YOLO model for ₹10, ₹20, ₹50, ₹100, ₹200 and ₹500 recognition.
