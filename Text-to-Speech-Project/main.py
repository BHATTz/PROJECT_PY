import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

# Example usage
while True:
    text = input("Enter something to hear (or 'q' to quit): ")
    if text == "q":
        text_to_speech("Quitting the program. Goodbye!")
        break

    text_to_speech(text)