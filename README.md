# VisionVoice AI: Smart Assistant for the Visually Impaired

VisionVoice AI is an AI-based assistive system designed to help visually impaired people understand their surroundings using a combination of **computer vision, voice recognition, OCR, and text-to-speech technology**.

The system can identify common objects through a camera, read text from images, and provide information through spoken feedback. The project is also being extended to recognize **Indian currency denominations** using a custom-trained AI model.

---

##  Project Objective

The main objective of VisionVoice AI is to provide a simple and accessible assistant that helps visually impaired users:

* Identify objects around them.
* Read text from images.
* Receive information through voice.
* Interact with the system using voice commands.
* Identify Indian currency notes.
* Improve independence in everyday activities.

---

## Features

### Currently Implemented

* ✅ Image-based object detection
* ✅ Real-time camera object detection
* ✅ YOLO-based object recognition
* ✅ Confidence-based detection filtering
* ✅ Stable object detection before voice announcement
* ✅ Text-to-speech output
* ✅ EasyOCR-based text recognition
* ✅ CPU-based AI processing

### In Development

* 🔄 Indian currency recognition
* 🔄 Custom YOLO model training
* 🔄 Currency detection accuracy evaluation
* 🔄 OCR-to-voice integration
* 🔄 Voice commands
* 🔄 Complete Vision + Voice interaction

### Planned Features

* 🔲 Hindi voice support
* 🔲 Medicine/label recognition
* 🔲 Face recognition
* 🔲 Color identification
* 🔲 Improved scene understanding
* 🔲 Android mobile application
* 🔲 Offline support for major features

---

# Technologies Used

| Technology | Purpose                                      |
| ---------- | -------------------------------------------- |
| Python     | Main programming language                    |
| YOLO11     | Object detection                             |
| OpenCV     | Camera and image processing                  |
| EasyOCR    | Text recognition                             |
| pyttsx3    | Text-to-speech                               |
| PyTorch    | Deep learning framework used by AI libraries |
| VS Code    | Development environment                      |
| Git/GitHub | Version control                              |

---

#  AI Components

## 1. Object Detection — YOLO11

A pretrained YOLO11 model is currently being used to detect common objects.

Examples:

* Person
* Laptop
* Cell phone
* Bottle
* Chair
* Other supported objects

The current system uses the pretrained:

```text
yolo11n.pt
```

The model does not need to be trained from scratch for general object detection.

### Detection Flow

```text
Camera / Image
      ↓
YOLO11
      ↓
Object Detection
      ↓
Object Name + Confidence
      ↓
Voice Output
```

---

## 2. Confidence Filtering

The system currently uses a confidence threshold to reduce unreliable detections.

Current threshold:

```text
0.60
```

Predictions below the selected threshold are ignored.

This helps reduce false-positive detections.

---

## 3. Stable Detection

The camera system does not immediately announce every detection.

The object needs to remain detected across multiple frames before the system announces it.

This helps prevent repeated or unstable announcements such as:

```text
Bottle
Toothbrush
Bottle
Toothbrush
Bottle
```

Instead, the system waits for a stable detection before speaking.

---

#  Text-to-Speech

The project uses `pyttsx3` for local text-to-speech.

Example:

```text
YOLO detects:

person
cell phone

↓

VisionVoice AI

↓

"I can see a person and cell phone."

↓

Computer Speaker
```

The speech engine runs locally and does not require a paid API.

---

#  OCR — Text Recognition

EasyOCR is being used to extract text from images.

Example:

```text
Image
   ↓
EasyOCR
   ↓
"VISIONVOICE AI"
```

The detected text is currently displayed in the terminal.

The next step is to connect the OCR result with the text-to-speech module so that the system can read the detected text aloud.

---

# 🇮🇳 Indian Currency Recognition

Indian currency recognition is an important feature of the project.

The planned system will recognize:

```text
₹10
₹20
₹50
₹100
₹200
₹500
```

A custom YOLO model will be trained for these denominations.

### Planned Training Process

```text
Currency Images
      ↓
Image Annotation
      ↓
Dataset Preparation
      ↓
Train / Validation / Test Split
      ↓
Custom YOLO Training
      ↓
Model Validation
      ↓
Accuracy Evaluation
      ↓
Currency Detection
      ↓
Voice Output
```

Example final behavior:

```text
Camera
   ↓
Custom Currency Model
   ↓
₹500
   ↓
Text-to-Speech
   ↓
"This is a 500 rupee note."
```

The currency dataset is currently being prepared.

---

# 📁 Project Structure

```text
Vision Voice AI/
│
├── images/
│   └── test.jpg
│
├── models/
│
├── modules/
│   ├── object_detection.py
│   ├── ocr.py
│   ├── speech.py
│   └── __pycache__/
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
├── README.md
├── requirements.txt
└── yolo11n.pt
```

---

# ⚙️ Current Development Environment

```text
Python: 3.13.14
YOLO: YOLO11
OpenCV: 5.0.0
OCR: EasyOCR
Text-to-Speech: pyttsx3
Development Environment: VS Code
Operating System: Windows
```

The project currently runs AI processing on the CPU when a supported GPU accelerator is not available.

---

# 🚀 Installation

## 1. Clone the project

```bash
git clone <repository-url>
cd "Vision Voice AI"
```

## 2. Create virtual environment

```bash
py -3.13 -m venv venv
```

## 3. Activate virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

If dependencies have not yet been saved:

```bash
pip install ultralytics opencv-python pyttsx3 easyocr
```

---

# ▶ Running the Project

## Object Detection on an Image

Place an image inside:

```text
images/test.jpg
```

Run:

```bash
python modules/object_detection.py
```

The system detects objects and displays their confidence scores.

Example:

```text
Detected Objects:

person
laptop
bottle

Assistant: I can see person, laptop, bottle.
```

---

## Real-Time Camera Detection

Run:

```bash
python camera_detection.py
```

The webcam opens and YOLO detects objects in real time.

Press:

```text
Q
```

to close the camera.

---

## OCR Testing

Place a text-containing image inside:

```text
images/
```

Then run:

```bash
python modules/ocr.py
```

The system extracts visible text using EasyOCR.

---

#  APIs and Cost

The current implementation primarily uses **local/open-source libraries**.

No paid AI API is required for the current prototype.

The project uses:

* YOLO locally
* OpenCV locally
* EasyOCR locally
* pyttsx3 locally

Therefore, the core prototype can be developed without recurring API charges.

---

# Accuracy Improvement

Object detection performance can be improved through:

* Increasing the quality and diversity of training data.
* Using different lighting conditions.
* Using different backgrounds.
* Capturing objects from different angles.
* Adding different object sizes and distances.
* Data augmentation.
* Fine-tuning YOLO on a custom dataset.
* Removing incorrect annotations.
* Evaluating precision and recall.
* Testing on previously unseen images.

For Indian currency recognition, a dedicated dataset will be created and evaluated separately.

---

#  Future Scope

The project can be extended with:

1. Indian currency recognition.
2. Medicine recognition.
3. Face recognition.
4. Voice-based commands.
5. Hindi and English language support.
6. Scene description.
7. Color identification.
8. Barcode and QR code recognition.
9. Emergency assistance.
10. Android mobile application.
11. Offline AI processing.
12. Smart-glasses integration.

---

#  Project Concept

VisionVoice AI combines two major interaction methods:

```text
             VISION
                +
              VOICE
                ↓
         VISIONVOICE AI
                ↓
        Assistive Feedback
```

The vision component understands the user's surroundings, while the voice component communicates the information to the user.

---



| Component                 | Status         |
| ------------------------- | -------------- |
| Python environment        | ✅ Completed    |
| Virtual environment       | ✅ Completed    |
| YOLO installation         | ✅ Completed    |
| General object detection  | ✅ Completed    |
| Image detection           | ✅ Completed    |
| Live camera detection     | ✅ Completed    |
| Confidence filtering      | ✅ Completed    |
| Stable detection          | ✅ Completed    |
| Text-to-speech            | ✅ Completed    |
| EasyOCR installation      | ✅ Completed    |
| OCR text detection        | ✅ Tested       |
| OCR voice output          | 🔄 In progress |
| Currency dataset          | 🔄 In progress |
| Currency annotation       | ⏳ Pending      |
| Currency model training   | ⏳ Pending      |
| Currency accuracy testing | ⏳ Pending      |
| Voice commands            | ⏳ Pending      |
| Android application       | ⏳ Pending      |

---

# 🎓 Project Goal

The final goal of VisionVoice AI is to create an accessible AI assistant that can **see, understand, and speak** information to visually impaired users.

The final system will combine:

```text
Camera
   ↓
Computer Vision
   ↓
Object / Currency / Text Recognition
   ↓
AI Processing
   ↓
Voice Response
   ↓
User
```

The project aims to provide a practical, affordable, and user-friendly assistive solution using AI and open-source technologies.
