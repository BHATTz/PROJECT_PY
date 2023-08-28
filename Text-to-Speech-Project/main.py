# import pyttsx3

# def text_to_speech(text):
#     engine = pyttsx3.init()  # Initialize the text-to-speech engine
#     engine.setProperty('rate', 100)  # Set the speed of speech (words per minute)
#     engine.setProperty('volume', 1.0)  # Set the volume (0.0 to 1.0)
#     engine.say(text)  # Queue the text to be spoken
#     engine.runAndWait()  # Speak the queued text

# # Example usage
# while True:
#     text = input("Enter something to hear (or 'q' to quit): ")  # Prompt the user for input
#     if text == "q":
#         text_to_speech("Quitting the program. Goodbye!")  # Speak the goodbye message
#         break  # Exit the loop

#     text_to_speech(text)  # Speak the input text

import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    engine.setProperty('rate', 100)  # Set the speed of speech (words per minute)
    engine.setProperty('volume', 1.0)  # Set the volume (0.0 to 1.0)
    engine.say(text)  # Queue the text to be spoken
    engine.runAndWait()  # Speak the queued text

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            text_to_speech(content)
    except FileNotFoundError:
        print("File not found.")

# Example usage
while True:
    choice = input("Enter 'f' to process a file, 'q' to quit: ")
    
    if choice == 'q':
        text_to_speech("Quitting the program. Goodbye!")
        break
    
    if choice == 'f':
        file_path = input("Enter the path to the text file: ")
        process_file(file_path)
    else:
        print("Invalid choice.")
