import cv2
from ultralytics import YOLO
from modules.speech import speak
import time


# ==========================================
# Load YOLO
# ==========================================

model = YOLO("yolo11n.pt")


# ==========================================
# Open Camera
# ==========================================

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()


# ==========================================
# Detection Settings
# ==========================================

CONFIDENCE_THRESHOLD = 0.60

# Same detection must remain stable
STABLE_FRAMES_REQUIRED = 8

# Minimum time between announcements
SPEECH_COOLDOWN = 4


# ==========================================
# Variables
# ==========================================

last_spoken_objects = set()

candidate_objects = set()

stable_frame_count = 0

last_speech_time = 0


# ==========================================
# Camera Loop
# ==========================================

while True:

    success, frame = camera.read()

    if not success:
        print("Error: Could not read camera.")
        break


    # ======================================
    # YOLO Detection
    # ======================================

    results = model(
        frame,
        conf=CONFIDENCE_THRESHOLD,
        verbose=False
    )


    # Draw bounding boxes
    annotated_frame = results[0].plot()


    # ======================================
    # Get Current Objects
    # ======================================

    current_objects = set()

    for box in results[0].boxes:

        class_id = int(box.cls[0])

        confidence = float(box.conf[0])

        object_name = results[0].names[class_id]

        if confidence >= CONFIDENCE_THRESHOLD:

            current_objects.add(object_name)


    # ======================================
    # Check Detection Stability
    # ======================================

    if current_objects == candidate_objects:

        stable_frame_count += 1

    else:

        candidate_objects = current_objects

        stable_frame_count = 1


    # ======================================
    # Voice Decision
    # ======================================

    current_time = time.time()

    if (
        stable_frame_count >= STABLE_FRAMES_REQUIRED
        and current_objects
        and current_objects != last_spoken_objects
        and current_time - last_speech_time >= SPEECH_COOLDOWN
    ):

        # Sort objects so message is consistent
        objects = sorted(current_objects)


        # Create natural sentence
        if len(objects) == 1:

            message = f"I can see a {objects[0]}."

        else:

            message = "I can see " + ", ".join(objects[:-1])

            message += f", and {objects[-1]}."


        # Speak
        speak(message)


        # Remember what we spoke
        last_spoken_objects = current_objects.copy()

        last_speech_time = time.time()


    # ======================================
    # Show Camera
    # ======================================

    cv2.imshow(
        "VisionVoice AI - Camera",
        annotated_frame
    )


    # ======================================
    # Quit
    # ======================================

    if cv2.waitKey(1) & 0xFF == ord("q"):

        break


# ==========================================
# Release Camera
# ==========================================

camera.release()

cv2.destroyAllWindows()