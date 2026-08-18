from ultralytics import YOLO
from speech import speak


# Load pretrained YOLO model
model = YOLO("yolo11n.pt")


# Analyze image
results = model("images/test.jpg")


detected_objects = []


for result in results:

    for box in result.boxes:

        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        object_name = result.names[class_id]

        # Only accept reasonably confident detections
        if confidence >= 0.50:
            detected_objects.append(object_name)


# Remove duplicate objects
detected_objects = list(set(detected_objects))


print("\nDetected Objects:")

for obj in detected_objects:
    print(obj)


# Create voice response
if detected_objects:

    if len(detected_objects) == 1:
        message = f"I can see a {detected_objects[0]}."

    else:
        objects_text = ", ".join(detected_objects)
        message = f"I can see {objects_text}."

else:
    message = "I could not identify any object."


# Speak the result
speak(message)