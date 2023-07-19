Here's a complete Python code for a text-to-speech project using the pyttsx3 library:

import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.8)  # Volume (0.0 to 1.0)

    engine.say(text)
    engine.runAndWait()

# Example usage
text = "Hello, how are you?"
text_to_speech(text)

Make sure you have the pyttsx3 library installed before running this code. You can install it using pip install pyttsx3.

This code initializes the pyttsx3 engine, sets the speech rate and volume, and then uses the say() method to convert the given text into speech. Finally, the runAndWait() function is called to play the speech output.

You can customize the speed and volume by adjusting the values in the setProperty() methods.

Feel free to modify this code according to your requirements.




