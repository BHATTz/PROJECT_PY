import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    engine.setProperty('rate', 90)  # Set the speed of speech (words per minute)
    engine.setProperty('volume', 1.0)  # Set the volume (0.0 to 1.0)
    engine.say(text)  # Queue the text to be spoken
    engine.runAndWait()  # Speak the queued text

# Example usage
while True:
    text = input("Enter something to hear (or 'q' to quit): ")  # Prompt the user for input
    if text == "q":
        text_to_speech("Quitting the program. Goodbye!")  # Speak the goodbye message
        break  # Exit the loop

    text_to_speech(text)  # Speak the input text