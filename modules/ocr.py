import easyocr
import cv2

# Create OCR reader
reader = easyocr.Reader(['en'])


def read_text(image_path):

    # Read text from image
    results = reader.readtext(image_path)

    detected_text = []

    for detection in results:

        text = detection[1]
        confidence = detection[2]

        if confidence >= 0.40:
            detected_text.append(text)

    return detected_text


if __name__ == "__main__":

    image_path = "images/test.jpg"

    text = read_text(image_path)

    print("\nDetected Text:")

    if text:
        for line in text:
            print(line)
    else:
        print("No text detected.")