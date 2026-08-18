import pyttsx3


def speak(text):
    print("Assistant:", text)

    try:
        # Create a fresh speech engine for each message
        engine = pyttsx3.init()

        # Voice settings
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 1.0)

        # Speak
        engine.say(text)
        engine.runAndWait()

        # Stop the engine cleanly
        engine.stop()

    except Exception as e:
        print("Speech error:", e)