from googletrans import Translator, LANGUAGES


def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, src="auto", dest=target_language)
    return translated.text


def get_supported_languages():
    return LANGUAGES


# Get user input
input_text = input("Enter the text you want to translate: ")
target_language = input("Enter the target language (e.g., 'es' for Spanish): ")

if target_language in get_supported_languages():
    translated_text = translate_text(input_text, target_language)
    print(f"Translated text: {translated_text}")
else:
    print("Invalid target language. Please choose a valid language code.")
